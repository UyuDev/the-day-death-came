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
    "good ending 1": pygame.image.load("assets/placeholder.png").convert_alpha(),

    # art items
    "small_chest": pygame.image.load("assets/chest_temp.png").convert_alpha(),
    "tomb": pygame.image.load("assets/chest_temp.png").convert_alpha(),
    "chest": pygame.image.load("assets/chest_temp.png").convert_alpha(),
    "crate": pygame.image.load("assets/chest_temp.png").convert_alpha(),
    "crates": pygame.image.load("assets/chest_temp.png").convert_alpha(),
    "altar": pygame.image.load("assets/chest_temp.png").convert_alpha(),

    # art enemies
    "unknown_enemy": pygame.image.load("assets/unknown_enemy_temp.png").convert_alpha(),
    "bandit": pygame.image.load("assets/bandit.png").convert_alpha(),
    "giant_rat": pygame.image.load("assets/rat_temp.png").convert_alpha(),
    "cave_goblin": pygame.image.load("assets/goblin.png").convert_alpha(),
    "skeleton": pygame.image.load("assets/bandit_temp.png").convert_alpha(),
    "zombie": pygame.image.load("assets/bandit_temp.png").convert_alpha(),
    "skeleton_warrior": pygame.image.load("assets/bandit_temp.png").convert_alpha(),
    "cultist_acolyte": pygame.image.load("assets/bandit_temp.png").convert_alpha(),
    "skeleton_mage": pygame.image.load("assets/bandit_temp.png").convert_alpha(),
    "honor_guard": pygame.image.load("assets/bandit_temp.png").convert_alpha(),
    "lord_graye": pygame.image.load("assets/bandit_temp.png").convert_alpha(),
    "reaper_boss_spawn": pygame.image.load("assets/bandit_temp.png").convert_alpha(),
    "reaper_boss_1": pygame.image.load("assets/bandit_temp.png").convert_alpha(),
    "reaper_boss_2": pygame.image.load("assets/bandit_temp.png").convert_alpha(),
    "reaper_boss_3": pygame.image.load("assets/bandit_temp.png").convert_alpha(),
    "reaper_boss_4": pygame.image.load("assets/bandit_temp.png").convert_alpha(),

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
    "town": pygame.image.load("assets/town_map_WIP.png").convert_alpha(),
    "crypt 1": pygame.image.load("assets/crypt_map_1.png").convert_alpha(),
    "crypt 2": pygame.image.load("assets/crypt_map_2.png").convert_alpha(),
    "crypt 3": pygame.image.load("assets/crypt_map_boss.png").convert_alpha(),
    "farm outside": pygame.image.load("assets/farm_map.png").convert_alpha(),

    # tiles
    "f": pygame.image.load("assets/stone_floor.png").convert_alpha(),
    "d": pygame.image.load("assets/wood_door_3.png").convert_alpha(),
    "b": pygame.image.load("assets/bed.png").convert_alpha(),
    "D": pygame.image.load("assets/wood_dungeon_1.png").convert_alpha(),
    "S": pygame.image.load("assets/wood_stairs_2.png").convert_alpha(), # wood stairs
    "9": pygame.image.load("assets/wood_stairs_1.png").convert_alpha(), # wood stairs
    "t": pygame.image.load("assets/wood_table_1.png").convert_alpha(), # wood table
    "1": pygame.image.load("assets/wood_wall_4.png").convert_alpha(),
    "T": pygame.image.load("assets/tools.png").convert_alpha(),
    "E": pygame.image.load("assets/dungeon_door.png").convert_alpha(),
    "C": pygame.image.load("assets/chest_tile.png").convert_alpha(),
    "L": pygame.image.load("assets/ladder.png").convert_alpha(),
    "B": pygame.image.load("assets/bookshelf.png").convert_alpha(),
    "W": pygame.image.load("assets/wood_wall_4.png").convert_alpha(), # wood floor
    "R": pygame.image.load("assets/crate.png").convert_alpha(),  # crate
    # Farm
    "r": pygame.image.load("assets/farm_ground.png").convert_alpha(),
    "v": pygame.image.load("assets/farm_fence.png").convert_alpha(),  # fence
    "-": pygame.image.load("assets/farm_grass.png").convert_alpha(),  # grass 1
    "+": pygame.image.load("assets/farm_tree_1.png").convert_alpha(),  # tree 1
    "*": pygame.image.load("assets/farm_tree_2.png").convert_alpha(),  # tree 2


    # Cave
    "c": pygame.image.load("assets/cave_1.png").convert_alpha(),
    "y": pygame.image.load("assets/cave_2.png").convert_alpha(),
    "Y": pygame.image.load("assets/cave_3.png").convert_alpha(),

    # Sewer
    "s": pygame.image.load("assets/sewer_1.png").convert_alpha(),  # sewer wall
    "h": pygame.image.load("assets/sewer_bed.png").convert_alpha(),  # straw bed
    "g": pygame.image.load("assets/sewer_1.png").convert_alpha(),  # stone ground
    "w": pygame.image.load("assets/sewer_water.png").convert_alpha(),  # water
    "H": pygame.image.load("assets/sewer_door.png").convert_alpha(),  # heavy door
    "=": pygame.image.load("assets/sewer_bridge.png").convert_alpha(),  # stone bridge

    # Dungeon
    "F": pygame.image.load("assets/stone_floor.png").convert_alpha(),  # stone floor
    "P": pygame.image.load("assets/prison_cell.png").convert_alpha(),  # prison cell
    "u": pygame.image.load("assets/wood_table_1.png").convert_alpha(),  # wood table
    ">": pygame.image.load("assets/tunnel_steps.png").convert_alpha(),  # tunnel steps
    "<": pygame.image.load("assets/tunnel_steps_2.png").convert_alpha(),  # tunnel steps 2

    # Town
    "V": pygame.image.load("assets/wattle_wall.png").convert_alpha(),  # wattle-and-daub wall
    "U": pygame.image.load("assets/wattle_wall_2.png").convert_alpha(),  # wattle-and-daub wall 2
    "X": pygame.image.load("assets/wattle_wall_3.png").convert_alpha(),  # wattle-and-daub wall 3
    "x": pygame.image.load("assets/wattle_wall_4.png").convert_alpha(),  # wattle-and-daub wall 4
    "J": pygame.image.load("assets/wattle_wall_5.png").convert_alpha(),  # wattle-and-daub wall 5   
    "?": pygame.image.load("assets/wattle_wall_close.png").convert_alpha(),  # wattle-and-daub wall closeup   
    "^": pygame.image.load("assets/roof.png").convert_alpha(),  # roof
    "G": pygame.image.load("assets/graves_1.png").convert_alpha(),  # gravestone
    "Q": pygame.image.load("assets/graves_2.png").convert_alpha(),  # gravestone 2
    "I": pygame.image.load("assets/stone_wall.png").convert_alpha(),  # stone wall
    "j": pygame.image.load("assets/stone_road_2.png").convert_alpha(),  # dirt road
    "_": pygame.image.load("assets/dirt_road_2.png").convert_alpha(),  # dirt road 2
    "$": pygame.image.load("assets/dirt_road_3.png").convert_alpha(),  # dirt road 3
    "&": pygame.image.load("assets/dirt_road_4.png").convert_alpha(),  # dirt road 4
    "O": pygame.image.load("assets/church_1.png").convert_alpha(),  # church
    "N": pygame.image.load("assets/fort_1.png").convert_alpha(),  # fortress / keep
    "l": pygame.image.load("assets/fort_2.png").convert_alpha(),  # fortress / keep   
    "Z": pygame.image.load("assets/fort_3.png").convert_alpha(),  # fortress / keep

    # Crypt
    "q": pygame.image.load("assets/crypt_1.png").convert_alpha(),  # crypt floor 1
    "e": pygame.image.load("assets/crypt_1.png").convert_alpha(),  # crypt floor 2
    "i": pygame.image.load("assets/crypt_1.png").convert_alpha(),  # crypt floor 3
    "K": pygame.image.load("assets/crypt_1.png").convert_alpha(),  # crypt wall
    "m": pygame.image.load("assets/crypt_tomb.png").convert_alpha(),  # sarcophagus
    "z": pygame.image.load("assets/crypt_fire.png").convert_alpha(),  # brazier
    "A": pygame.image.load("assets/crypt_altar.png").convert_alpha(),  # altar
    "M": pygame.image.load("assets/crypt_tomb_2.png").convert_alpha(),  # ornate tomb
}

