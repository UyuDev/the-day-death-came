import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, FPS
from grid import Grid
from scene import Scene
from assets import load_assets
from menu import Menu
from save import SaveMenu, load_save, can_save, save_game, apply_save, SAVE_LOCATIONS, reload_current_save
from dialogue import Dialogue
from settings import load_settings, save_settings, edit_settings, load_language
from character import Character
from actions import handle_action
from world_state import WorldState
from exploration import Exploration

def main():
    print(f"Starting Fantasy RPG with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    settings = load_settings()
    language_data = load_language(settings["language"])
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    assets = load_assets()
    clock = pygame.time.Clock()
    ui_font = pygame.font.Font("assets/fonts/Rockboxcond12.ttf", 24)
    title_font = pygame.font.Font("assets/fonts/Bitfantasy.ttf", 48)
    #create grid
    if settings["art"] == "tiles":
        renderer = Grid(assets)
    else:
        renderer = Scene(assets)
    menu = Menu(language_data, assets)
    save_menu = SaveMenu(language_data, assets)
    dialogue = Dialogue(language_data, assets)
    exploration = Exploration(language_data, assets)
    player = Character()
    player.create("Nicholas", 1, "Classless", None, 0, None)
    world_state = WorldState()
    game_state = "MENU"
    #update with game loop
    while True:
        #log if implemented
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            
            #draw map
            
            #draw objects
            if game_state == "MENU":
                choice = menu.handle_input(event)
                if choice == 1:
                    renderer.load_map("house_upstairs")
                    player = Character()
                    player.create("Nicholas", 1, "Classless", None, 0, None)
                    world_state = WorldState()
                    dialogue.set_current("intro")
                    game_state = "INTRO"
                elif choice == 2:
                    game_state = "SAVE MENU"
                elif choice == 3:
                    # settings
                    game_state = "SETTINGS"
                elif choice == 4:
                    return
            elif game_state == "SETTINGS":
                choice = menu.handle_input(event)
                # ignore random events so only keypressed are passed 
                if choice is not None:
                    if choice == 4:
                        game_state = "MENU"
                    else:
                        result = edit_settings(settings, choice)
                        if choice == 1:
                            language_data = load_language(settings["language"])
                            menu.language_data = language_data
                            dialogue.language_data = language_data
                            save_menu.language_data = language_data
                        if choice == 2:
                            print("Hardcore mode is now implemented!")
                        if choice == 3:
                            if settings["art"] == "tiles":
                                renderer = Grid(assets)
                            else:
                                renderer = Scene(assets)
                        save_settings(result)
                    # if result:
                        # some other action
            # WIP
            elif game_state == "SAVE MENU":
                choice = save_menu.handle_input(event)
                # ignore random events so only keypressed are passed 
                if choice is not None:
                    if choice == "new_game":
                        renderer.load_map("house_upstairs")
                        player = Character()
                        player.create("Nicholas", 1, "Classless", None, 0, None)
                        world_state = WorldState()
                        dialogue.set_current("intro")
                        game_state = "INTRO"
                    elif choice == "load_game":
                        checkpoint = SAVE_LOCATIONS[world_state.save_location]

                        renderer.load_map(checkpoint["map"])
                        dialogue.set_current(checkpoint["dialogue"])
                        game_state = "INTRO"
                    elif choice == 4:
                        game_state = "MENU"
                    elif choice == 3:
                        save_menu.change_page()
                    else:
                        if choice == 1 and save_menu.page == 1:
                            save_data = load_save(1)
                            save_menu.current_slot = 1
                            save_menu.set_current(save_data)
                        elif choice == 2 and save_menu.page == 1:
                            save_data = load_save(2)
                            save_menu.current_slot = 2
                            save_menu.set_current(save_data)
                        elif choice == 1 and save_menu.page == 2:
                            save_data = load_save(3)
                            save_menu.current_slot = 3
                            save_menu.set_current(save_data)
                        elif choice == 2 and save_menu.page == 2:
                            save_data = load_save(4)
                            save_menu.current_slot = 4
                            save_menu.set_current(save_data)
                        if save_data is not None:
                            apply_save(save_data, player, world_state)


            elif game_state == "INTRO":
                choice = None
                if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                    print("Inventory:")
                    print(player.inventory)
                    print("Keyring:")
                    print(player.keyring)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                    print("Equipment:")
                    print(player.equipped)
                elif dialogue.has_options():
                    choice = dialogue.handle_input(event)
                else:
                    choice = dialogue.handle_input_continue(event)
                # ignore random events so only keypressed are passed 
                if choice is not None:
                    dialogue.advance(choice)
                    actions = dialogue.get_actions()
                    for action in actions:
                        result = handle_action(action, player, renderer, dialogue, world_state, save_menu, settings, exploration)
                        if result is not None:
                            if result == "HARDCORE_DEATH":
                                player = Character()
                                player.create("Nicholas", 1, "Classless", None, 0, None)
                                world_state = WorldState()
                                renderer.load_map("house_upstairs")
                                dialogue.set_current("hardcore death reset")
                                game_state = "INTRO"
                                save_game(
                                    player,
                                    world_state.flags,
                                    world_state.save_location,
                                    save_menu.current_slot,
                                    dialogue.language_data
                                )
                                break
                            else:
                                game_state = result
                                break

            elif game_state == "EXPLORATION":
                choice = None
                if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                    print("Inventory:")
                    print(player.inventory)
                    print("Keyring:")
                    print(player.keyring)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                    print("Equipment:")
                    print(player.equipped)
                else:
                    choice = exploration.handle_input_continue(event)
                # ignore random events so only keypressed are passed 
                if choice is not None:
                    result = exploration.advance(choice)
                    if result is not None:
                        if result == "death":
                            if settings["hardcore"]:

                                player = Character()
                                player.create("Nicholas", 1, "Classless", None, 0, None)
                                world_state = WorldState()
                                renderer.load_map("house_upstairs")
                                dialogue.set_current("hardcore death reset")
                                game_state = "INTRO"
                                save_game(
                                    player,
                                    world_state.flags,
                                    world_state.save_location,
                                    save_menu.current_slot,
                                    exploration.language_data
                                )
                            else:
                                reload_current_save(
                                    player,
                                    world_state,
                                    save_menu,
                                    renderer,
                                    dialogue
                                )
                                world_state.flags["has_died"] = True
                        game_state = "INTRO"
                    


        # grid.draw(screen)
        screen.fill((BACKGROUND_COLOR))
        if game_state == "MENU":
            # renderer.draw(screen)
            menu.draw(screen, title_font, ui_font)

        elif game_state == "SETTINGS":
            # renderer.draw(screen)
            menu.draw_settings(screen, title_font, ui_font, settings)

        elif game_state == "SAVE MENU":
            save_menu.draw_options(screen, title_font, ui_font)

        elif game_state == "INTRO":
            renderer.draw(screen)
            dialogue.draw(screen, ui_font, player)

        elif game_state == "EXPLORATION":
            # renderer.draw(screen)
            exploration.draw(screen, ui_font, player)

        pygame.display.flip()
        clock.tick(FPS)





if __name__ == "__main__":
    main()
