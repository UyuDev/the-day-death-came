from item_data import ITEMS, EQUIPMENT_TEMPLATES





ENEMIES = {
    "tunnel_bandit": {
        "name": "Bandit Ambusher",
        "level": 1,
        "game_class": "Rogue",
        "inventory": ["Cheese"],
        "coins": 5,
        "equipped": EQUIPMENT_TEMPLATES["light_armor"],
        "image": "bandit"
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
    "sewer_bandit": {
        "name": "Bandit",
        "level": 5,
        "game_class": "Rogue",
        "inventory": ["Rogue Tools"],
        "coins": 1,
        "equipped": EQUIPMENT_TEMPLATES["light_armor"],
        "image": "bandit"
    },
    "dungeon_bandit": {
        "name": "Bandit",
        "level": 7,
        "game_class": "Rogue",
        "inventory": ["Dungeon Keys"],
        "coins": 1,
        "equipped": EQUIPMENT_TEMPLATES["light_armor"],
        "image": "bandit"
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
        "inventory": ["Crystal fragment"],
        "coins": 10,
        "equipped": EQUIPMENT_TEMPLATES["cultist"],
        "image": "cultist_acolyte"
    },
    "skeleton_warrior": {
        "name": "Skeleton Warrior",
        "level": 15,
        "game_class": "Warrior",
        "inventory": ["Bones", "Crystal fragment"],
        "coins": 15,
        "equipped": EQUIPMENT_TEMPLATES["skeleton_warrior"],
        "image": "skeleton_warrior"
    },
    "skeleton_mage": {
        "name": "Skeleton mage",
        "level": 15,
        "game_class": "Mage",
        "inventory": ["Bones", "Crystal fragment"],
        "coins": 15,
        "equipped": EQUIPMENT_TEMPLATES["skeleton_mage"],
        "image": "skeleton_mage"
    },
    "skeleton_knight": {
        "name": "Skeleton Knight",
        "level": 20,
        "game_class": "Warrior",
        "inventory": ["Bones", "Crystal fragment"],
        "coins": 20,
        "equipped": EQUIPMENT_TEMPLATES["skeleton_warrior"],
        "image": "skeleton_warrior"
    },
    "skeleton_darkmaster": {
        "name": "Skeleton Darkmaster",
        "level": 20,
        "game_class": "Warlock",
        "inventory": ["Bones", "Crystal fragment"],
        "coins": 20,
        "equipped": EQUIPMENT_TEMPLATES["skeleton_mage"],
        "image": "skeleton_mage"
    },
    "farm_bandit": {
        "name": "Bandit",
        "level": 10,
        "game_class": "Warrior",
        "inventory": ["Stolen Goods"],
        "coins": 5,
        "equipped": EQUIPMENT_TEMPLATES["light_armor"],
        "image": "bandit"
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
        "game_class": "Reaper",
        "inventory": ["Ancient Armament"],
        "coins": 100,
        "equipped": EQUIPMENT_TEMPLATES["reaper"],
        "image": "reaper_boss_1"
    },
    "reaper_boss_2": {
        "name": "Sa, the Hungering Reaper",
        "level": 50,
        "game_class": "Reaper",
        "inventory": ["Ancient Armament", "Ancient Armament"],
        "coins": 250,
        "equipped": EQUIPMENT_TEMPLATES["reaper"],
        "image": "reaper_boss_2"
    },
    "reaper_boss_3": {
        "name": "Sa, the Furious Reaper",
        "level": 75,
        "game_class": "Reaper",
        "inventory": ["Ancient Armament", "Ancient Armament", "Ancient Armament"],
        "coins": 500,
        "equipped": EQUIPMENT_TEMPLATES["reaper"],
        "image": "reaper_boss_3"
    },
    "reaper_boss_4": {
        "name": "Sa, the Unleashed Reaper",
        "level": 100,
        "game_class": "Reaper",
        "inventory": ["Ancient Armament", "Ancient Armament", "Ancient Armament", "Ancient Armament"],
        "coins": 1000,
        "equipped": EQUIPMENT_TEMPLATES["reaper"],
        "image": "reaper_boss_4"
    }
}