import pygame
from constants import TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, MAP_HEIGHT
from map_dict import MAPS


class Grid:
    def __init__(self, assets):
        self.width = SCREEN_WIDTH // TILE_SIZE
        self.height = MAP_HEIGHT // TILE_SIZE
        self.grid = []
        self.assets = assets
        self.current_scene = None
        self.scene_active = False
        self.previous_scene = None
        self.setup_grid()

    def setup_grid(self):
        for i in range(self.height):
            self.grid.append([])
            for _ in range(self.width):
                self.grid[i].append("0")

    def load_map(self, map):
        self.scene_active = False
        if map not in MAPS:
            raise NotImplementedError("This map hasn't been implemented")
        self.grid = MAPS[map]


    def show_scene(self, scene):
        self.previous_scene = self.current_scene
        if scene not in self.assets:
            raise NotImplementedError("This scene hasn't been implemented")
        self.current_scene = pygame.transform.scale(self.assets[scene], (SCREEN_WIDTH, MAP_HEIGHT))
        self.scene_active = True


    def clear_scene(self):
        if self.scene_active:
            self.current_scene = self.previous_scene
            self.previous_scene = None
            self.scene_active = False



    def draw(self, screen):
        if self.scene_active == True:
            screen.blit(self.current_scene, (0, 0))
        else:
            for y, row in enumerate(self.grid):
                for x, tile in enumerate(row):
                    if tile == "0":
                        rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                        pygame.draw.rect(screen, "black", rect) 
                    else:
                        image = self.assets[tile]
                        screen.blit(
                            image,
                            (x * TILE_SIZE, y * TILE_SIZE)
                        ) 



    
