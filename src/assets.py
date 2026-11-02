import pygame




def load_assets():
    return {
    "menuscreen_art": pygame.image.load("assets/main_menu.png").convert_alpha(),
    "ui_image": pygame.image.load("assets/game_ui.png").convert_alpha(),

    # death illustrations - omitted for v1
    # "trapdoor death": pygame.image.load("assets/black_map.png").convert_alpha(), 
    # "collapse book": pygame.image.load("assets/black_map.png").convert_alpha(),
    # "door death spear": pygame.image.load("assets/black_map.png").convert_alpha(),
    # "door death arrow": pygame.image.load("assets/black_map.png").convert_alpha(), 
    # "door death leg": pygame.image.load("assets/black_map.png").convert_alpha(),
    # "door death mind": pygame.image.load("assets/black_map.png").convert_alpha(),
    # "door death collapse": pygame.image.load("assets/black_map.png").convert_alpha(),
    # "good ending 1": pygame.image.load("assets/black_map.png").convert_alpha(),

    # Container illustrations
    "chest": pygame.image.load("assets/chest_container.png").convert_alpha(),
    "crate": pygame.image.load("assets/crate_container.png").convert_alpha(),
    # "crates": pygame.image.load("assets/crate_container.png").convert_alpha(),

    # Enemy illustrations
    "unknown_enemy": pygame.image.load("assets/unknown_enemy.png").convert_alpha(),
    "dungeon_inmate": pygame.image.load("assets/dungeon_inmate.png").convert_alpha(),
    "invader_warrior": pygame.image.load("assets/invader_warrior.png").convert_alpha(),
    "invader_rogue": pygame.image.load("assets/invader_rogue.png").convert_alpha(),
    "invader_ranger": pygame.image.load("assets/invader_ranger.png").convert_alpha(),
    "invader_warlock": pygame.image.load("assets/invader_warlock.png").convert_alpha(),
    "invader_reaver": pygame.image.load("assets/invader_reaver.png").convert_alpha(),
    "giant_rat": pygame.image.load("assets/giant_rat.png").convert_alpha(),
    "cave_goblin": pygame.image.load("assets/cave_goblin.png").convert_alpha(),
    "skeleton": pygame.image.load("assets/skeleton.png").convert_alpha(),
    "zombie": pygame.image.load("assets/zombie.png").convert_alpha(),
    "skeleton_warrior": pygame.image.load("assets/skeleton_warrior.png").convert_alpha(),
    "skeleton_knight": pygame.image.load("assets/skeleton_knight.png").convert_alpha(),
    "cultist_acolyte": pygame.image.load("assets/cultist.png").convert_alpha(),
    "skeleton_mage": pygame.image.load("assets/skeleton_mage.png").convert_alpha(),
    "skeleton_warlock": pygame.image.load("assets/skeleton_warlock.png").convert_alpha(),
    "honor_guard": pygame.image.load("assets/honor_guard.png").convert_alpha(),
    "lord_graye": pygame.image.load("assets/lord_graye.png").convert_alpha(),
    "reaper_boss_spawn": pygame.image.load("assets/reaper_spawn.png").convert_alpha(),
    "reaper_boss_1": pygame.image.load("assets/reaper_boss_1.png").convert_alpha(),
    "reaper_boss_2": pygame.image.load("assets/reaper_boss_2.png").convert_alpha(),
    "reaper_boss_3": pygame.image.load("assets/reaper_boss_3.png").convert_alpha(),
    "reaper_boss_4": pygame.image.load("assets/reaper_boss_4.png").convert_alpha(),

    # Maps
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

    # Tiles

    # House
    "f": pygame.image.load("assets/red_brick_floor.png").convert_alpha(), # basement floor
    "d": pygame.image.load("assets/house_interior_door.png").convert_alpha(),
    "b": pygame.image.load("assets/bed.png").convert_alpha(),
    "D": pygame.image.load("assets/red_brick_trapdoor.png").convert_alpha(),
    "S": pygame.image.load("assets/upstairs_staircase.png").convert_alpha(), # upstairs staricase
    "9": pygame.image.load("assets/downstairs_staircase.png").convert_alpha(), # downstairs staircase
    "t": pygame.image.load("assets/wood_table.png").convert_alpha(), # wood table
    "1": pygame.image.load("assets/house_interior_wall.png").convert_alpha(),
    "T": pygame.image.load("assets/red_brick_tools.png").convert_alpha(),
    "E": pygame.image.load("assets/basement_door.png").convert_alpha(),
    "L": pygame.image.load("assets/red_brick_ladder.png").convert_alpha(),
    "B": pygame.image.load("assets/bookshelf.png").convert_alpha(),
    "W": pygame.image.load("assets/wood_floor.png").convert_alpha(), # wood floor

    # Containers
    "C": pygame.image.load("assets/chest.png").convert_alpha(),
    "R": pygame.image.load("assets/crate.png").convert_alpha(),  # crate

    # New house
    "ㅂ": pygame.image.load("assets/house_partition_wall.png").convert_alpha(), # part wall
    "ㅁ": pygame.image.load("assets/house_partition_door.png").convert_alpha(), # part door
    "ㄹ": pygame.image.load("assets/house_kitchen_range.png").convert_alpha(), # kitchen
    "ㅎ": pygame.image.load("assets/house_hearth.png").convert_alpha(), # fireplace
    "ㅊ": pygame.image.load("assets/red_brick_hunting_chest.png").convert_alpha(), # hunting chest
    "ㅈ": pygame.image.load("assets/red_brick_chair.png").convert_alpha(), # chair
    "ㄷ": pygame.image.load("assets/house_window.png").convert_alpha(), # window



    # Farm
    "r": pygame.image.load("assets/farm_crops.png").convert_alpha(),
    "v": pygame.image.load("assets/farm_fence.png").convert_alpha(),  # fence
    "-": pygame.image.load("assets/farm_grass.png").convert_alpha(),  
    "?": pygame.image.load("assets/house_entrance.png").convert_alpha(),  # farmhouse 
    "2": pygame.image.load("assets/house_l.png").convert_alpha(), # house
    "3": pygame.image.load("assets/farm_granary.png").convert_alpha(), # granary

    # Flora
    "+": pygame.image.load("assets/tree_dark_1.png").convert_alpha(), 
    "*": pygame.image.load("assets/tree_dark_2.png").convert_alpha(),  # variant
    ",": pygame.image.load("assets/treeline_dark.png").convert_alpha(), # treeline trunks

    # Cave
    "c": pygame.image.load("assets/cave_floor.png").convert_alpha(),
    "y": pygame.image.load("assets/cave_stalagmites_1.png").convert_alpha(),
    "Y": pygame.image.load("assets/cave_stalagmites_2.png").convert_alpha(),
    "H": pygame.image.load("assets/metal_stone_door.png").convert_alpha(),  # heavy door
    "ㅏ": pygame.image.load("assets/cave_tent.png").convert_alpha(), # cave tent
    "ㅓ": pygame.image.load("assets/cave_crevice.png").convert_alpha(), # cave crevice


    # Sewer
    "h": pygame.image.load("assets/sewer_bed.png").convert_alpha(),  # straw bed
    "g": pygame.image.load("assets/sewer_floor.png").convert_alpha(),  # sewer stone ground
    "w": pygame.image.load("assets/sewer_water.png").convert_alpha(),  # water
    "=": pygame.image.load("assets/sewer_bridge.png").convert_alpha(),  # stone bridge

    # Dungeon
    "F": pygame.image.load("assets/red_brick_floor.png").convert_alpha(),  # dungeon floor
    "P": pygame.image.load("assets/dungeon_cell.png").convert_alpha(),  # cell
    "e": pygame.image.load("assets/red_brick_steps_v.png").convert_alpha(), # brick steps vertical
    "i": pygame.image.load("assets/red_brick_steps_h.png").convert_alpha(), # brick steps horizontal

    # Town
    "V": pygame.image.load("assets/townhouse_1.png").convert_alpha(),  # wattle-and-daub house
    "U": pygame.image.load("assets/townhouse_2.png").convert_alpha(),  # wattle-and-daub house 2
    "X": pygame.image.load("assets/townhouse_3.png").convert_alpha(),  # wattle-and-daub house 3
    "x": pygame.image.load("assets/townhouse_4.png").convert_alpha(),  # wattle-and-daub house 4
    "J": pygame.image.load("assets/townhouse_5.png").convert_alpha(),  # wattle-and-daub house 5   
    "[": pygame.image.load("assets/roof.png").convert_alpha(), # townhouse roof
    "^": pygame.image.load("assets/roof_center.png").convert_alpha(), # townhouse full roof
    "j": pygame.image.load("assets/stone_floor.png").convert_alpha(),  # stone floor - town and crypt
    "N": pygame.image.load("assets/fort_center.png").convert_alpha(),  # fortress center
    "l": pygame.image.load("assets/fort_l.png").convert_alpha(),  # fortress left
    "Z": pygame.image.load("assets/fort_r.png").convert_alpha(),  # fortress right
    "u": pygame.image.load("assets/fort_roof.png").convert_alpha(), # fortress roof

    # Town walls
    "4": pygame.image.load("assets/town_wall_tl.png").convert_alpha(),  # top-left
    "5": pygame.image.load("assets/town_wall_hb.png").convert_alpha(),   # horizontal
    "6": pygame.image.load("assets/town_wall_tr.png").convert_alpha(),  # top-right
    "7": pygame.image.load("assets/town_gate.png").convert_alpha(),   # vertical gate
    "8": pygame.image.load("assets/town_wall_bl.png").convert_alpha(),  # bottom-left
    "a": pygame.image.load("assets/town_wall_br.png").convert_alpha(),  # bottom-right
    "k": pygame.image.load("assets/town_wall_vl.png").convert_alpha(), # wall left
    "n": pygame.image.load("assets/town_wall_vr.png").convert_alpha(), # wall right
    "o": pygame.image.load("assets/town_wall_ht.png").convert_alpha(), # wall top

    # Town ground
    "!": pygame.image.load("assets/grass_green.png").convert_alpha(),  # green grass
    "@": pygame.image.load("assets/grass_dead.png").convert_alpha(),  # dead cemetery grass
    "#": pygame.image.load("assets/grass_flowers.png").convert_alpha(),  # flowering grass

    # Town exterior
    "]": pygame.image.load("assets/town_bridge.png").convert_alpha(), # bridge
    ":": pygame.image.load("assets/town_water.png").convert_alpha(), # water
    ";": pygame.image.load("assets/town_fountain.png").convert_alpha(), # fountain

    # Church tiles
    "O": pygame.image.load("assets/church_front.png").convert_alpha(),  # church entrance
    "~": pygame.image.load("assets/church_roof_center.png").convert_alpha(), 
    "{": pygame.image.load("assets/church_l.png").convert_alpha(),
    "}": pygame.image.load("assets/church_r.png").convert_alpha(),
    "|": pygame.image.load("assets/church_roof_top.png").convert_alpha(), 
    "G": pygame.image.load("assets/graves_1.png").convert_alpha(),  # gravestone
    "Q": pygame.image.load("assets/graves_2.png").convert_alpha(),  # gravestone 2
    "p": pygame.image.load("assets/crypt_entrance.png").convert_alpha(),

    # Crypt
    "<": pygame.image.load("assets/stone_stairs_v.png").convert_alpha(),  # stone steps vertical
    ">": pygame.image.load("assets/stone_stairs_h.png").convert_alpha(),  # stone steps horizontal
    "q": pygame.image.load("assets/crypt_floor.png").convert_alpha(),  # crypt floor 1
    "m": pygame.image.load("assets/crypt_tomb.png").convert_alpha(),  # sarcophagus
    "z": pygame.image.load("assets/crypt_brazier.png").convert_alpha(),  # brazier

    # Below the Church
    "A": pygame.image.load("assets/church_altar.png").convert_alpha(),  # altar
    "M": pygame.image.load("assets/ornate_tomb.png").convert_alpha(),  # ornate tomb
    ".": pygame.image.load("assets/church_pillar.png").convert_alpha(), # pillar    
    "I": pygame.image.load("assets/church_floor.png").convert_alpha(),  # church floor

    # Unused backups
    # "$": pygame.image.load("assets/dirt_road_3.png").convert_alpha(),
    # "&": pygame.image.load("assets/dirt_road_4.png").convert_alpha(), 
    # ")": pygame.image.load("assets/grass_dead_2.png").convert_alpha(), 
    # "(": pygame.image.load("assets/grass_green_2.png").convert_alpha(), 
    # "%": pygame.image.load("assets/grass_flowers_2.png").convert_alpha(),
    # "s": pygame.image.load("assets/sewer_1.png").convert_alpha(), 
    # "_": pygame.image.load("assets/house_partition_wall_v.png").convert_alpha(), # vertical wall
    # "K": pygame.image.load("assets/house_partition_door_v.png").convert_alpha(),  # vertical door
}

