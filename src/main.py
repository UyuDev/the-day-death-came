import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, FPS
from grid import Grid
from assets import load_assets
from menu import Menu

def main():
    print(f"Starting Fantasy RPG with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    tile_images = load_assets()
    clock = pygame.time.Clock()
    dt = 0.0
    ui_font = pygame.font.Font("assets/fonts/Rockboxcond12.ttf", 24)
    title_font = pygame.font.Font("assets/fonts/Bitfantasy.ttf", 48)
    #create grid
    grid = Grid(tile_images)
    menu = Menu()
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
                    grid.load_map("house")
                    game_state = "INTRO"
                elif choice == 2:
                    # game_state = "LOAD"
                    print("Not yet implemented")
                elif choice == 3:
                    return
        
        

        # grid.draw(screen)
        screen.fill((BACKGROUND_COLOR))
        if game_state == "MENU":
            grid.draw(screen)
            menu.draw(screen, title_font, ui_font)

        elif game_state == "INTRO":
            grid.draw(screen)

        pygame.display.flip()
        dt = clock.tick(FPS) / 1000





if __name__ == "__main__":
    main()
