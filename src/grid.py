import pygame
from enum import Enum
from constants import TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, MAP_HEIGHT
from maps import house_map

class TileType(Enum):
    BLANK = "black"
    FLOOR = 90, 60, 35
    WALL = 150, 105, 65
    DOOR = 90, 60, 35



class Grid:
    def __init__(self):
        self.width = SCREEN_WIDTH // TILE_SIZE
        self.height = MAP_HEIGHT // TILE_SIZE
        self.grid = []

    def setup_grid(self):
        for i in range(self.height):
            self.grid.append([])
            for j in range(self.width):
                tile = Tile(TileType.BLANK, j, i)
                self.grid[i].append(tile)

    def load_map(self, map):
        x = 0
        y = 0
        if map == "house":
            for row in house_map:
                # the height is 5 chars which needs to become 10, so double
                for i in range(1): # was 2
                    for char in row:
                        # the width is 8 chars which needs to become 8 out of 32, so keep the same and do 12 blank on each side
                        if char == "b":
                            for j in range(12):
                                blank_tile = Tile(TileType.BLANK, x, y)
                                self.grid[y][x] = blank_tile
                                x += 1
                        elif char == "#":
                            wall_tile = Tile(TileType.WALL, x, y)
                            self.grid[y][x] = wall_tile
                            x += 1
                        elif char == ".":
                            floor_tile = Tile(TileType.FLOOR, x, y)
                            self.grid[y][x] = floor_tile
                            x += 1
                        elif char == "d":
                            door_tile = Tile(TileType.DOOR, x, y)
                            self.grid[y][x] = door_tile
                            x += 1
                    y += 1
                    x = 0
        else:
            raise NotImplementedError("This map hasn't been implemented")

                    

    def draw(self, screen):
        for row in self.grid:
            for tile in row:
                rect = pygame.Rect(tile.x * TILE_SIZE, tile.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, tile.color, rect)       



class Tile:
    def __init__(self, tile_type: TileType, x: int, y: int):
        self.type = tile_type
        self.x = x
        self.y =y
        self.color = tile_type.value

    def __str__(self):
        return f"({self.x},{self.y})"


    
