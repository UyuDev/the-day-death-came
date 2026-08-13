import pygame




def load_assets():
    return {
    "f": pygame.image.load("assets/stone_floor.png").convert_alpha(),
    "d": pygame.image.load("assets/wood_door_2.png").convert_alpha(),
    "D": pygame.image.load("assets/wood_dungeon_1.png").convert_alpha(),
    "S": pygame.image.load("assets/wood_stairs_1.png").convert_alpha(),
    "t": pygame.image.load("assets/wood_table_1.png").convert_alpha(),
    "1": pygame.image.load("assets/wood_wall_3.png").convert_alpha(),
}

