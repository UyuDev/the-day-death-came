import pygame


class WorldState():
    def __init__(self):
        self.flags = {
            "basement_unlocked": False,
            "bed_chest_empty": False,
            "inventory_unlocked": False,
            "dresser_empty": False,
            "left_bookshelf_empty": False,
            "forbidden_book_taken": False,
            "combat_treatise_taken": False,
            "downstairs_boots_taken": False,
            "downstairs_table_empty": False,
            "downstairs_chest_empty": False,
            "downstairs_fireplace_empty": False,
            "basement_tools_empty": False,
            "dungeon_door_unlocked": False,
            "crypt_door_unlocked": False
        }