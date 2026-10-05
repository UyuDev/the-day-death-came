from item_data import ITEMS, EQUIPMENT_TEMPLATES





ENEMIES = {
    "tunnel_ambusher": {
        "name": "Invading Ambusher",
        "level": 1,
        "game_class": "Rogue",
        "inventory": ["Cryptic Letter"],
        "coins": 5,
        "equipped": EQUIPMENT_TEMPLATES["invader_rogue"],
        "image": "invader_rogue"
    },
    "giant_rat": {
        "name": "Giant Rat",
        "level": 1,
        "game_class": "Beast",
        "inventory": ["Rat Meat", "Fang"],
        "coins": 1,
        "equipped": EQUIPMENT_TEMPLATES["None"],
        "image": "giant_rat"
    },
    "cave_goblin": {
        "name": "Cave Goblin",
        "level": 3,
        "game_class": "Warrior",
        "inventory": ["Cave Mushroom"],
        "coins": 1,
        "equipped": EQUIPMENT_TEMPLATES["goblin"],
        "image": "cave_goblin"
    },
    "sewer_invader_rogue": {
        "name": "Invading Rogue",
        "level": 5,
        "game_class": "Rogue",
        "inventory": ["Lockpick"],
        "coins": 5,
        "equipped": EQUIPMENT_TEMPLATES["invader_rogue"],
        "image": "invader_rogue"
    },
    "dungeon_rogue": {
        "name": "Invading Rogue",
        "level": 10,
        "game_class": "Rogue",
        "inventory": ["Lockpick"],
        "coins": 10,
        "equipped": EQUIPMENT_TEMPLATES["invader_rogue"],
        "image": "invader_rogue"
    },
    "town_rogue": {
        "name": "Invading Rogue",
        "level": 10,
        "game_class": "Rogue",
        "inventory": ["Lockpick"],
        "coins": 10,
        "equipped": EQUIPMENT_TEMPLATES["invader_rogue"],
        "image": "invader_rogue"
    },
    "sewer_invader_ranger": {
        "name": "Invading Ranger",
        "level": 5,
        "game_class": "Ranger",
        "inventory": ["Ranger Traps"],
        "coins": 5,
        "equipped": EQUIPMENT_TEMPLATES["invader_ranger"],
        "image": "invader_ranger"
    },
    "town_ranger": {
        "name": "Invading Ranger",
        "level": 10,
        "game_class": "Ranger",
        "inventory": ["Ranger Traps"],
        "coins": 10,
        "equipped": EQUIPMENT_TEMPLATES["invader_ranger"],
        "image": "invader_ranger"
    },
    "dungeon_invader_warlock": {
        "name": "Invading Warlock",
        "level": 7,
        "game_class": "Warlock",
        "inventory": ["Strange Relic"],
        "coins": 1,
        "equipped": EQUIPMENT_TEMPLATES["invader_warlock"],
        "image": "invader_warlock"
    },
    "town_warlock": {
        "name": "Invading Warlock",
        "level": 10,
        "game_class": "Warlock",
        "inventory": ["Strange Relic"],
        "coins": 10,
        "equipped": EQUIPMENT_TEMPLATES["invader_warlock"],
        "image": "invader_warlock"
    },
    "elite_invader_caster": {
        "name": "Invading Elite Caster",
        "level": 30,
        "game_class": "Warlock",
        "inventory": ["Strange Relic"],
        "coins": 1,
        "equipped": EQUIPMENT_TEMPLATES["invader_warlock"],
        "image": "invader_warlock"
    },
    "dungeon_invader_warrior": {
        "name": "Invading Warrior",
        "level": 7,
        "game_class": "Warrior",
        "inventory": ["Sharpening Stone"],
        "coins": 1,
        "equipped": EQUIPMENT_TEMPLATES["invader_warrior"],
        "image": "invader_warrior"
    },
    "town_warrior": {
        "name": "Invading Warrior",
        "level": 10,
        "game_class": "Warrior",
        "inventory": ["Sharpening Stone"],
        "coins": 10,
        "equipped": EQUIPMENT_TEMPLATES["invader_warrior"],
        "image": "invader_warrior"
    },
    "dungeon_inmate": {
        "name": "Released Inmate",
        "level": 7,
        "game_class": "Rogue",
        "inventory": ["Stale Bread"],
        "coins": 0,
        "equipped": EQUIPMENT_TEMPLATES["prisoner"],
        "image": "dungeon_inmate"
    },
    "skeleton": {
        "name": "Skeleton",
        "level": 8,
        "game_class": "Warrior",
        "inventory": ["Bones"],
        "coins": 0,
        "equipped": EQUIPMENT_TEMPLATES["skeleton_sword"],
        "image": "skeleton"
    },
    "zombie": {
        "name": "Zombie",
        "level": 8,
        "game_class": "Warrior",
        "inventory": ["Bones"],
        "coins": 0,
        "equipped": EQUIPMENT_TEMPLATES["None"],
        "image": "zombie"
    },
    "skeleton_fighter": {
        "name": "Skeleton Fighter",
        "level": 10,
        "game_class": "Warrior",
        "inventory": ["Bones"],
        "coins": 0,
        "equipped": EQUIPMENT_TEMPLATES["skeleton_sword"],
        "image": "skeleton_warrior"
    },
    "cultist_acolyte": {
        "name": "Cultist Acolyte",
        "level": 10,
        "game_class": "Warlock",
        "inventory": ["Crystal Fragment"],
        "coins": 10,
        "equipped": EQUIPMENT_TEMPLATES["cultist"],
        "image": "cultist_acolyte"
    },
    "skeleton_warrior": {
        "name": "Skeleton Warrior",
        "level": 15,
        "game_class": "Warrior",
        "inventory": ["Bones"],
        "coins": 15,
        "equipped": EQUIPMENT_TEMPLATES["skeleton_warrior"],
        "image": "skeleton_warrior"
    },
    "skeleton_mage": {
        "name": "Skeleton mage",
        "level": 15,
        "game_class": "Mage",
        "inventory": ["Bones", "Magic Ashes"],
        "coins": 15,
        "equipped": EQUIPMENT_TEMPLATES["skeleton_mage"],
        "image": "skeleton_mage"
    },
    "skeleton_knight": {
        "name": "Skeleton Knight",
        "level": 20,
        "game_class": "Warrior",
        "inventory": ["Bones"],
        "coins": 20,
        "equipped": EQUIPMENT_TEMPLATES["skeleton_knight"],
        "image": "skeleton_knight"
    },
    "skeleton_darkmaster": {
        "name": "Skeleton Darkmaster",
        "level": 20,
        "game_class": "Warlock",
        "inventory": ["Bones", "Crystal Fragment"],
        "coins": 20,
        "equipped": EQUIPMENT_TEMPLATES["skeleton_mage"],
        "image": "skeleton_warlock"
    },
    "farm_invader_rogue": {
        "name": "Invading Rogue",
        "level": 15,
        "game_class": "Rogue",
        "inventory": ["Lockpick"],
        "coins": 10,
        "equipped": EQUIPMENT_TEMPLATES["invader_rogue"],
        "image": "invader_rogue"
    },
    "farm_invader_ranger": {
        "name": "Invading Ranger",
        "level": 15,
        "game_class": "Ranger",
        "inventory": ["Ranger Traps"],
        "coins": 10,
        "equipped": EQUIPMENT_TEMPLATES["invader_ranger"],
        "image": "invader_ranger"
    },
    "farm_invader_warrior": {
        "name": "Invading Warrior",
        "level": 15,
        "game_class": "Warrior",
        "inventory": ["Sharpening Stone"],
        "coins": 10,
        "equipped": EQUIPMENT_TEMPLATES["invader_warrior"],
        "image": "invader_warrior"
    },
    "farm_invader_warlock": {
        "name": "Invading Warlock",
        "level": 15,
        "game_class": "Warlock",
        "inventory": ["Strange Relic"],
        "coins": 10,
        "equipped": EQUIPMENT_TEMPLATES["invader_warlock"],
        "image": "invader_warlock"
    },
    "invader_captain": {
        "name": "Reaver Captain",
        "level": 20,
        "game_class": "Reaver",
        "inventory": ["Invader's Orders"],
        "coins": 25,
        "equipped": EQUIPMENT_TEMPLATES["invader_reaver"],
        "image": "invader_reaver"
    },
    "honor_guard": {
        "name": "Honor Guard",
        "level": 20,
        "game_class": "Paladin",
        "inventory": ["Prayer Book"],
        "coins": 25,
        "equipped": EQUIPMENT_TEMPLATES["honor_guard"],
        "image": "honor_guard"
    },
    "lord_graye": {
        "name": "Lord Graye",
        "level": 20,
        "game_class": "Mage",
        "inventory": ["Rare jewels"],
        "coins": 100,
        "equipped": EQUIPMENT_TEMPLATES["lord"],
        "image": "lord_graye"
    },
    "reaper_boss_1": {
        "name": "Sa, the Banished Reaper",
        "level": 30,
        "game_class": "ReaperBoss",
        "inventory": ["Ancient Armament"],
        "coins": 100,
        "equipped": EQUIPMENT_TEMPLATES["None"],
        "image": "reaper_boss_1"
    },
    "reaper_boss_2": {
        "name": "Sa, the Hungering Reaper",
        "level": 100,
        "game_class": "ReaperBoss",
        "inventory": ["Ancient Armament", "Ancient Armament"],
        "coins": 1000,
        "equipped": EQUIPMENT_TEMPLATES["None"],
        "image": "reaper_boss_2"
    },
    "reaper_boss_3": {
        "name": "Sa, the Furious Reaper",
        "level": 250,
        "game_class": "ReaperBoss",
        "inventory": ["Ancient Armament", "Ancient Armament", "Ancient Armament"],
        "coins": 10000,
        "equipped": EQUIPMENT_TEMPLATES["None"],
        "image": "reaper_boss_3"
    },
    "reaper_boss_4": {
        "name": "Sa, the Unleashed Reaper",
        "level": 999,
        "game_class": "ReaperBoss",
        "inventory": ["Ancient Armament", "Ancient Armament", "Ancient Armament", "Ancient Armament"],
        "coins": 99999,
        "equipped": EQUIPMENT_TEMPLATES["None"],
        "image": "reaper_boss_4"
    }
}