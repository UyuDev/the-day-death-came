import pygame
from enum import Enum
from constants import TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, MAP_HEIGHT
from map_dict import MAPS

class TileColors(Enum):
    BLANK = "black"
    FLOOR = 81, 57, 24
    DOOR = 181, 173, 166
    BED = 181, 173, 166
    DUNGEON = 50, 56, 50
    STAIRS = 90, 60, 35
    TABLE = 90, 60, 35
    WALL = 163, 123, 90
    TOOLS = "black"
    DUNGEONENT = "black"
    CHEST = "black"
    BOOKSHELF = "black"
    WOODFLOOR = "black"



TILE_MAPPING = {
    "0": TileColors.BLANK,
    "f": TileColors.FLOOR,
    "W": TileColors.WOODFLOOR,
    "d": TileColors.DOOR,
    "b": TileColors.BED,
    "D": TileColors.DUNGEON,
    "S": TileColors.STAIRS,
    "t": TileColors.TABLE,
    "1": TileColors.WALL,
    "T": TileColors.TOOLS,
    "E": TileColors.DUNGEONENT,
    "C": TileColors.CHEST,
    "B": TileColors.BOOKSHELF,
}




class Grid:
    def __init__(self, assets):
        self.width = SCREEN_WIDTH // TILE_SIZE
        self.height = MAP_HEIGHT // TILE_SIZE
        self.grid = []
        self.assets = assets
        self.current_scene = None
        self.scene_active = False
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

    def load_scene(self, scene):
        if scene not in self.assets:
            raise NotImplementedError("This scene hasn't been implemented")
        self.current_scene = pygame.transform.scale(self.assets[scene], (SCREEN_WIDTH, MAP_HEIGHT))
        self.scene_active = True

    def clear_scene(self):
        self.current_scene = None
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

    def draw_rect(self, screen):
            for y, row in enumerate(self.grid):
                for x, tile in enumerate(row):
                    rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    pygame.draw.rect(screen, TILE_MAPPING[tile].value, rect)       


class Tile:
    def __init__(self, tile_type: TileColors, x: int, y: int):
        self.type = tile_type
        self.x = x
        self.y = y
        self.color = tile_type.value

    def __str__(self):
        return f"({self.x},{self.y})"


    
