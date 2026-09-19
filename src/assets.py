import pygame




def load_assets():
    return {
    "menuscreen_art": pygame.image.load("assets/main_temp_b.png").convert_alpha(),
    "ui_image": pygame.image.load("assets/UI_temp_2.png").convert_alpha(),

    # art deaths
    "trapdoor death": pygame.image.load("assets/trapdoor_burn_temp.png").convert_alpha(), 
    "collapse book": pygame.image.load("assets/collapse_book_temp.png").convert_alpha(),
    "door death spear": pygame.image.load("assets/door_death_spear_temp.png").convert_alpha(),
    "door death arrow": pygame.image.load("assets/door_death_arrow_temp.png").convert_alpha(), 
    "door death leg": pygame.image.load("assets/door_death_leg_temp.png").convert_alpha(),
    "door death mind": pygame.image.load("assets/door_death_mind_temp.png").convert_alpha(),
    "door death collapse": pygame.image.load("assets/door_death_collapse_temp.png").convert_alpha(),

    # art items
    "small_chest": pygame.image.load("assets/chest_temp.png").convert_alpha(),
    "tomb": pygame.image.load("assets/chest_temp.png").convert_alpha(),
    "chest": pygame.image.load("assets/chest_temp.png").convert_alpha(),
    "crate": pygame.image.load("assets/chest_temp.png").convert_alpha(),
    "crates": pygame.image.load("assets/chest_temp.png").convert_alpha(),

    # art enemies
    "unknown_enemy": pygame.image.load("assets/unknown_enemy_temp.png").convert_alpha(),
    "bandit": pygame.image.load("assets/bandit_temp.png").convert_alpha(),
    "giant_rat": pygame.image.load("assets/rat_temp.png").convert_alpha(),
    "cave_goblin": pygame.image.load("assets/goblin_temp.png").convert_alpha(),
    "skeleton": pygame.image.load("assets/bandit_temp.png").convert_alpha(),
    "zombie": pygame.image.load("assets/bandit_temp.png").convert_alpha(),
    "skeleton_warrior": pygame.image.load("assets/bandit_temp.png").convert_alpha(),
    "cultist_acolyte": pygame.image.load("assets/bandit_temp.png").convert_alpha(),
    "skeleton_mage": pygame.image.load("assets/bandit_temp.png").convert_alpha(),
    "honor_guard": pygame.image.load("assets/bandit_temp.png").convert_alpha(),
    "lord_graye": pygame.image.load("assets/bandit_temp.png").convert_alpha(),
    "reaper_boss": pygame.image.load("assets/bandit_temp.png").convert_alpha(),

    # maps
    "house": pygame.image.load("assets/home_map.png").convert_alpha(),
    "house_upstairs": pygame.image.load("assets/upstairs_map.png").convert_alpha(),
    "basement": pygame.image.load("assets/basement_map.png").convert_alpha(),
    "basement 2": pygame.image.load("assets/basement_map_2.png").convert_alpha(),
    "pitch black": pygame.image.load("assets/basement_map.png").convert_alpha(),
    "tunnel 1": pygame.image.load("assets/tunnel_map_1.png").convert_alpha(),
    "tunnel 2": pygame.image.load("assets/tunnel_map_2.png").convert_alpha(),
    "sewer": pygame.image.load("assets/sewer_map.png").convert_alpha(),
    "dungeon": pygame.image.load("assets/dungeon_map.png").convert_alpha(),
    "crypt 1": pygame.image.load("assets/crypt_map_1.png").convert_alpha(),
    "crypt 2": pygame.image.load("assets/crypt_map_2.png").convert_alpha(),
    "crypt boss": pygame.image.load("assets/crypt_map_boss.png").convert_alpha(),
    "farm outside": pygame.image.load("assets/farm_map.png").convert_alpha(),

    # tiles
    "f": pygame.image.load("assets/stone_floor.png").convert_alpha(),
    "d": pygame.image.load("assets/wood_door_2.png").convert_alpha(),
    "b": pygame.image.load("assets/bed.png").convert_alpha(),
    "D": pygame.image.load("assets/wood_dungeon_1.png").convert_alpha(),
    "S": pygame.image.load("assets/wood_stairs_1.png").convert_alpha(),
    "t": pygame.image.load("assets/wood_table_1.png").convert_alpha(),
    "1": pygame.image.load("assets/wood_wall_3.png").convert_alpha(),
    "T": pygame.image.load("assets/placeholder.png").convert_alpha(),
    "E": pygame.image.load("assets/placeholder.png").convert_alpha(),
    "C": pygame.image.load("assets/placeholder.png").convert_alpha(),
    "L": pygame.image.load("assets/placeholder.png").convert_alpha(),
    "B": pygame.image.load("assets/placeholder.png").convert_alpha(),
    "W": pygame.image.load("assets/wood_floor_2.png").convert_alpha(),
}

