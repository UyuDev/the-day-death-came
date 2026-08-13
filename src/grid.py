import pygame
from enum import Enum
from constants import TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, MAP_HEIGHT
from map_dict import MAPS

class TileColors(Enum):
    BLANK = "black"
    FLOOR = 81, 57, 24
    DOOR = 181, 173, 166
    DUNGEON = 50, 56, 50
    STAIRS = 90, 60, 35
    TABLE = 90, 60, 35
    WALL = 163, 123, 90



TILE_MAPPING = {
    "0": TileColors.BLANK,
    "f": TileColors.FLOOR,
    "d": TileColors.DOOR,
    "D": TileColors.DUNGEON,
    "S": TileColors.STAIRS,
    "t": TileColors.TABLE,
    "1": TileColors.WALL,
}




class Grid:
    def __init__(self, tile_images):
        self.width = SCREEN_WIDTH // TILE_SIZE
        self.height = MAP_HEIGHT // TILE_SIZE
        self.grid = []
        self.tile_images = tile_images
        self.setup_grid()

    def setup_grid(self):
        for i in range(self.height):
            self.grid.append([])
            for _ in range(self.width):
                self.grid[i].append("0")

    def load_map(self, map):
        if map not in MAPS:
            raise NotImplementedError("This map hasn't been implemented")
        self.grid = MAPS[map]


                    

    def draw(self, screen):
        for y, row in enumerate(self.grid):
            for x, tile in enumerate(row):
                if tile == "0":
                    rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    pygame.draw.rect(screen, "black", rect) 
                else:
                    image = self.tile_images[tile]
                    screen.blit(
                        image,
                        (x * TILE_SIZE, y * TILE_SIZE)
                    ) 

    def draw_rect(self, screen):
            for y, row in enumerate(self.grid):
                for x, tile in enumerate(row):
                    rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    pygame.draw.rect(screen, TILE_MAPPING[tile].value, rect)       



class Tile:
    def __init__(self, tile_type: TileColors, x: int, y: int):
        self.type = tile_type
        self.x = x
        self.y =y
        self.color = tile_type.value

    def __str__(self):
        return f"({self.x},{self.y})"


    
