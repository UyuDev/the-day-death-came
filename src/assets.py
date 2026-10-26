import pygame




def load_assets():
    return {
    "menuscreen_art": pygame.image.load("assets/menu_art_1.png").convert_alpha(),
    "ui_image": pygame.image.load("assets/UI_temp_2.png").convert_alpha(),

    # art deaths
    "trapdoor death": pygame.image.load("assets/black_map.png").convert_alpha(), 
    "collapse book": pygame.image.load("assets/black_map.png").convert_alpha(),
    "door death spear": pygame.image.load("assets/black_map.png").convert_alpha(),
    "door death arrow": pygame.image.load("assets/black_map.png").convert_alpha(), 
    "door death leg": pygame.image.load("assets/black_map.png").convert_alpha(),
    "door death mind": pygame.image.load("assets/black_map.png").convert_alpha(),
    "door death collapse": pygame.image.load("assets/black_map.png").convert_alpha(),
    "good ending 1": pygame.image.load("assets/black_map.png").convert_alpha(),

    # art items
    "small_chest": pygame.image.load("assets/chest_temp.png").convert_alpha(),
    "tomb": pygame.image.load("assets/chest_temp.png").convert_alpha(),
    "chest": pygame.image.load("assets/chest_temp.png").convert_alpha(),
    "crate": pygame.image.load("assets/chest_temp.png").convert_alpha(),
    "crates": pygame.image.load("assets/chest_temp.png").convert_alpha(),
    "altar": pygame.image.load("assets/chest_temp.png").convert_alpha(),

    # art enemies
    "unknown_enemy": pygame.image.load("assets/unknown_enemy_2.png").convert_alpha(),
    "bandit": pygame.image.load("assets/bandit.png").convert_alpha(),
    "dungeon_inmate": pygame.image.load("assets/inmate_1.png").convert_alpha(),
    "invader_warrior": pygame.image.load("assets/invader_warr_1.png").convert_alpha(),
    "invader_rogue": pygame.image.load("assets/invader_rogue_1.png").convert_alpha(),
    "invader_ranger": pygame.image.load("assets/invader_ranger_1.png").convert_alpha(),
    "invader_warlock": pygame.image.load("assets/invader_warlock_1.png").convert_alpha(),
    "invader_reaver": pygame.image.load("assets/invader_reaver_2.png").convert_alpha(),
    "giant_rat": pygame.image.load("assets/rat_temp_2.png").convert_alpha(),
    "cave_goblin": pygame.image.load("assets/goblin_3.png").convert_alpha(),
    "skeleton": pygame.image.load("assets/skeleton_1.png").convert_alpha(),
    "zombie": pygame.image.load("assets/zombie_1.png").convert_alpha(),
    "skeleton_warrior": pygame.image.load("assets/skeleton_warr_1.png").convert_alpha(),
    "skeleton_knight": pygame.image.load("assets/skeleton_knight_1.png").convert_alpha(),
    "cultist_acolyte": pygame.image.load("assets/cultist_1.png").convert_alpha(),
    "skeleton_mage": pygame.image.load("assets/skeleton_mage_1.png").convert_alpha(),
    "skeleton_warlock": pygame.image.load("assets/skeleton_darkmaster_1.png").convert_alpha(),
    "honor_guard": pygame.image.load("assets/honor_guard_1.png").convert_alpha(),
    "lord_graye": pygame.image.load("assets/lord_graye_1.png").convert_alpha(),
    "reaper_boss_spawn": pygame.image.load("assets/reaper_spawn_v2.png").convert_alpha(),
    "reaper_boss_1": pygame.image.load("assets/reaper_boss_v3_1.png").convert_alpha(),
    "reaper_boss_2": pygame.image.load("assets/reaper_boss_v3_2.png").convert_alpha(),
    "reaper_boss_3": pygame.image.load("assets/reaper_boss_v3_3.png").convert_alpha(),
    "reaper_boss_4": pygame.image.load("assets/reaper_boss_v3_4.png").convert_alpha(),

    # maps
    "house": pygame.image.load("assets/home_map.png").convert_alpha(),
    "house_upstairs": pygame.image.load("assets/upstairs_map.png").convert_alpha(),
    "basement": pygame.image.load("assets/basement_map.png").convert_alpha(),
    "basement 2": pygame.image.load("assets/basement_map_2.png").convert_alpha(),
    "pitch black": pygame.image.load("assets/black_map.png").convert_alpha(),
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
    "f": pygame.image.load("assets/tunnel_steps_2c.png").convert_alpha(), # basement floor
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
    "r": pygame.image.load("assets/farm_ground_b.png").convert_alpha(),
    "v": pygame.image.load("assets/farm_fence_b.png").convert_alpha(),  # fence
    "-": pygame.image.load("assets/farm_grass.png").convert_alpha(),  # grass 1
    "+": pygame.image.load("assets/farm_tree_1b.png").convert_alpha(),  # tree 1
    "*": pygame.image.load("assets/farm_tree_2b.png").convert_alpha(),  # tree 2
    "?": pygame.image.load("assets/house_1.png").convert_alpha(),  # farmhouse 
    "2": pygame.image.load("assets/house_2.png").convert_alpha(), # house
    "3": pygame.image.load("assets/farm_granary_1.png").convert_alpha(), # granary
    ",": pygame.image.load("assets/farm_treeline_1.png").convert_alpha(), # treeline trunks

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
    ">": pygame.image.load("assets/tunnel_steps_b.png").convert_alpha(),  # tunnel steps
    "<": pygame.image.load("assets/tunnel_steps_2b.png").convert_alpha(),  # tunnel steps 2

    # Town
    "V": pygame.image.load("assets/wattle_wall_1b.png").convert_alpha(),  # wattle-and-daub wall
    "U": pygame.image.load("assets/wattle_wall_2b.png").convert_alpha(),  # wattle-and-daub wall 2
    "X": pygame.image.load("assets/wattle_wall_3b.png").convert_alpha(),  # wattle-and-daub wall 3
    "x": pygame.image.load("assets/wattle_wall_4b.png").convert_alpha(),  # wattle-and-daub wall 4
    "J": pygame.image.load("assets/wattle_wall_5b.png").convert_alpha(),  # wattle-and-daub wall 5   
    "^": pygame.image.load("assets/roof.png").convert_alpha(),  # roof
    "j": pygame.image.load("assets/stone_road_2.png").convert_alpha(),  # dirt road
    "_": pygame.image.load("assets/dirt_road_2.png").convert_alpha(),  # dirt road 2
    "$": pygame.image.load("assets/dirt_road_3.png").convert_alpha(),  # dirt road 3
    "&": pygame.image.load("assets/dirt_road_4.png").convert_alpha(),  # dirt road 4
    "N": pygame.image.load("assets/fort_1b.png").convert_alpha(),  # fortress / keep
    "l": pygame.image.load("assets/fort_2b.png").convert_alpha(),  # fortress / keep   
    "Z": pygame.image.load("assets/fort_3b.png").convert_alpha(),  # fortress / keep

    # Town walls
    "4": pygame.image.load("assets/town_wall_tl2.png").convert_alpha(),  # top-left
    "5": pygame.image.load("assets/town_wall_h.png").convert_alpha(),   # horizontal
    "6": pygame.image.load("assets/town_wall_tr2.png").convert_alpha(),  # top-right
    "7": pygame.image.load("assets/town_gate.png").convert_alpha(),   # vertical gate
    "8": pygame.image.load("assets/town_wall_bl2.png").convert_alpha(),  # bottom-left
    "a": pygame.image.load("assets/town_wall_br2.png").convert_alpha(),  # bottom-right
    "k": pygame.image.load("assets/town_wall_vc.png").convert_alpha(), # wall left
    "n": pygame.image.load("assets/town_wall_vb.png").convert_alpha(), # wall right
    "o": pygame.image.load("assets/town_wall_hb.png").convert_alpha(), # wall top

    # Town ground
    "!": pygame.image.load("assets/grass_green_2.png").convert_alpha(),  # green grass
    "@": pygame.image.load("assets/grass_dead_1.png").convert_alpha(),  # dead cemetery grass
    "#": pygame.image.load("assets/grass_flowers_1.png").convert_alpha(),  # flowering grass
    "%": pygame.image.load("assets/grass_flowers_2.png").convert_alpha(),  # flowering grass variation
    "(": pygame.image.load("assets/grass_green_2.png").convert_alpha(),  # green grass variation
    ")": pygame.image.load("assets/grass_dead_2.png").convert_alpha(),  # dead grass variation

    # Reserved town decorations
    "[": pygame.image.load("assets/roof_3.png").convert_alpha(), # roof 2
    "]": pygame.image.load("assets/town_bridge_1.png").convert_alpha(), # bridge
    ":": pygame.image.load("assets/town_water_1.png").convert_alpha(), # water
    ";": pygame.image.load("assets/town_fountain_1.png").convert_alpha(), # fountain

    # Church tiles
    "O": pygame.image.load("assets/church_1b.png").convert_alpha(),  # church
    "~": pygame.image.load("assets/church_5.png").convert_alpha(), #church roof 1
    "{": pygame.image.load("assets/church_3b.png").convert_alpha(),
    "}": pygame.image.load("assets/church_4b.png").convert_alpha(),
    "|": pygame.image.load("assets/church_2b.png").convert_alpha(),  # church roof 2
    "G": pygame.image.load("assets/graves_1b.png").convert_alpha(),  # gravestone
    "Q": pygame.image.load("assets/graves_2b.png").convert_alpha(),  # gravestone 2
    "p": pygame.image.load("assets/crypt_ext2.png").convert_alpha(),

    # Crypt
    "q": pygame.image.load("assets/crypt_1.png").convert_alpha(),  # crypt floor 1
    "e": pygame.image.load("assets/crypt_1.png").convert_alpha(),  # crypt floor 2
    "i": pygame.image.load("assets/crypt_1.png").convert_alpha(),  # crypt floor 3
    "K": pygame.image.load("assets/crypt_1.png").convert_alpha(),  # crypt wall
    "m": pygame.image.load("assets/crypt_tomb_1b.png").convert_alpha(),  # sarcophagus
    "z": pygame.image.load("assets/crypt_fire_c.png").convert_alpha(),  # brazier
    "A": pygame.image.load("assets/crypt_altar_b.png").convert_alpha(),  # altar
    "M": pygame.image.load("assets/crypt_tomb_2b.png").convert_alpha(),  # ornate tomb
    ".": pygame.image.load("assets/crypt_pillar_1a.png").convert_alpha(), # pillar    
    "I": pygame.image.load("assets/stone_road_1.png").convert_alpha(),  # stone floor




}

