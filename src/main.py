import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, FPS
from grid import Grid
from assets import load_assets

def main():
    print(f"Starting Fantasy RPG with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    tile_images = load_assets()
    clock = pygame.time.Clock()
    dt = 0.0
    #create grid
    grid = Grid(tile_images)
    grid.load_map("house")
    while True:
        #log if implemented
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((BACKGROUND_COLOR))
        #draw map
        grid.draw(screen)
        #draw objects
        pygame.display.flip()
        dt = clock.tick(FPS) / 1000





if __name__ == "__main__":
    main()
