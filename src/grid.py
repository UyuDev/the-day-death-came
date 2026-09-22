import pygame
from enum import Enum
from constants import TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, MAP_HEIGHT
from map_dict import MAPS

class TileColors(Enum):
    BLANK = "black"
    FLOOR = 81, 57, 24
    DOOR = 181, 173, 166
    BED = 181, 173, 166
    TRAPDOOR = 50, 56, 50
    STAIRS = 90, 60, 35
    TABLE = 90, 60, 35
    WALL = 163, 123, 90
    STONE_WALL = "black"
    B_STONE_WALL = "black"
    TOOLS = "black"
    DUNGEON_ENT = "black"
    CHEST = "black"
    BOOKSHELF = "black"
    WOOD_FLOOR = "black"
    LADDER = "black"
    FENCE = "black"
    FARM_GROUND = "black"
    CAVE_1 = "black"
    CAVE_2 = "black"
    CAVE_3 = "black"
    CRATE = "black"
    SEWER_WALL = "black"
    STRAW_BED = "black"
    STONE_GROUND = "black"
    WATER = "black"
    HEAVY_DOOR = "black"
    STONE_BRIDGE = "black"

    STONE_FLOOR = "black"
    PRISON_CELL = "black"
    WOOD_TABLE = "black"
    TUNNEL_STEPS = "black"

    CRYPT_FLOOR_1 = "black"
    CRYPT_FLOOR_2 = "black"
    CRYPT_FLOOR_3 = "black"
    CRYPT_WALL = "black"
    SARCOPHAGUS = "black"
    BRAZIER = "black"
    ALTAR = "black"
    ORNATE_TOMB = "black"

TILE_MAPPING = {
    "0": TileColors.BLANK,
    "f": TileColors.FLOOR,
    "W": TileColors.WOOD_FLOOR,
    "d": TileColors.DOOR,
    "b": TileColors.BED,
    "D": TileColors.TRAPDOOR,
    "L": TileColors.LADDER,
    "S": TileColors.STAIRS,
    "t": TileColors.TABLE,
    "1": TileColors.WALL,
    "2": TileColors.STONE_WALL,
    "3": TileColors.B_STONE_WALL,
    "T": TileColors.TOOLS,
    "E": TileColors.DUNGEON_ENT,
    "C": TileColors.CHEST,
    "B": TileColors.BOOKSHELF,
    "v": TileColors.FENCE,
    "r": TileColors.FARM_GROUND,
    "c": TileColors.CAVE_1,
    "y": TileColors.CAVE_2,
    "Y": TileColors.CAVE_3,
    "R": TileColors.CRATE,
    "s": TileColors.SEWER_WALL,
    "h": TileColors.STRAW_BED,
    "g": TileColors.STONE_GROUND,
    "w": TileColors.WATER,
    "H": TileColors.HEAVY_DOOR,
    "=": TileColors.STONE_BRIDGE,

    "F": TileColors.STONE_FLOOR,
    "P": TileColors.PRISON_CELL,
    "u": TileColors.WOOD_TABLE,
    ">": TileColors.TUNNEL_STEPS,

    "q": TileColors.CRYPT_FLOOR_1,
    "e": TileColors.CRYPT_FLOOR_2,
    "i": TileColors.CRYPT_FLOOR_3,
    "K": TileColors.CRYPT_WALL,
    "m": TileColors.SARCOPHAGUS,
    "z": TileColors.BRAZIER,
    "A": TileColors.ALTAR,
    "M": TileColors.ORNATE_TOMB,
}




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

    # def load_scene(self, scene):
    #     if scene not in self.assets:
    #         raise NotImplementedError("This scene hasn't been implemented")
    #     self.current_scene = pygame.transform.scale(self.assets[scene], (SCREEN_WIDTH, MAP_HEIGHT))
    #     self.scene_active = True

    # def clear_scene(self):
    #     self.current_scene = None
    #     self.scene_active = False

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


    
