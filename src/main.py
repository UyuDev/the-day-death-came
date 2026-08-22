import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, FPS
from grid import Grid
from assets import load_assets
from menu import Menu
from dialogue import Dialogue
from settings import load_settings, save_settings, edit_settings, load_language

def main():
    print(f"Starting Fantasy RPG with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    settings = load_settings()
    language_data = load_language(settings["language"])
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    tile_images = load_assets()
    clock = pygame.time.Clock()
    ui_font = pygame.font.Font("assets/fonts/Rockboxcond12.ttf", 24)
    title_font = pygame.font.Font("assets/fonts/Bitfantasy.ttf", 48)
    #create grid
    grid = Grid(tile_images)
    menu = Menu(language_data)
    dialogue = Dialogue(language_data)
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
                    grid.load_map("house_upstairs")
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
                    if choice == 3:
                        game_state = "MENU"
                    else:
                        result = edit_settings(settings, choice)
                        if choice == 1:
                            language_data = load_language(settings["language"])
                            menu.language_data = language_data
                            dialogue.language_data = language_data
                        save_settings(result)
                    # if result:
                        # some other action


            elif game_state == "INTRO":
                choice = dialogue.handle_input(event)
                # ignore random events so only keypressed are passed 
                if choice is not None:
                    result = dialogue.advance(choice)
                    if result:
                        grid.load_map(result)



        # grid.draw(screen)
        screen.fill((BACKGROUND_COLOR))
        if game_state == "MENU":
            grid.draw(screen)
            menu.draw(screen, title_font, ui_font)

        elif game_state == "SETTINGS":
            grid.draw(screen)
            menu.draw_settings(screen, title_font, ui_font, settings)

        elif game_state == "INTRO":
            grid.draw(screen)
            dialogue.draw(screen, ui_font)

        pygame.display.flip()
        clock.tick(FPS)





if __name__ == "__main__":
    main()
