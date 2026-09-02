import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, FPS
from grid import Grid
from scene import Scene
from assets import load_assets
from menu import Menu
from dialogue import Dialogue
from settings import load_settings, save_settings, edit_settings, load_language
from character import Character
from actions import handle_action
from world_state import WorldState

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
    dialogue = Dialogue(language_data)
    player = Character()
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
                    game_state = "INTRO"
                elif choice == 2:
                    # game_state = "LOAD"
                    print("Not yet implemented")
                elif choice == 3:
                    # settings
                    game_state = "SETTINGS"
                    print("Not yet implemented")
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
                        if choice == 2:
                            print("Not yet implemented.")
                        if choice == 3:
                            if settings["art"] == "tiles":
                                renderer = Grid(assets)
                            else:
                                renderer = Scene(assets)
                        save_settings(result)
                    # if result:
                        # some other action


            elif game_state == "INTRO":
                choice = None
                if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                    print(player.inventory)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
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
                        handle_action(action, player, renderer, dialogue, world_state)



        # grid.draw(screen)
        screen.fill((BACKGROUND_COLOR))
        if game_state == "MENU":
            # renderer.draw(screen)
            menu.draw(screen, title_font, ui_font)

        elif game_state == "SETTINGS":
            # renderer.draw(screen)
            menu.draw_settings(screen, title_font, ui_font, settings)

        elif game_state == "INTRO":
            renderer.draw(screen)
            dialogue.draw(screen, ui_font)

        pygame.display.flip()
        clock.tick(FPS)





if __name__ == "__main__":
    main()
