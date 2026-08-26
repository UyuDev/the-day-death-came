import pygame


class WorldState():
    def __init__(self):
        self.flags = {
            "basement_unlocked": False,
            "footlocker_empty": False,
            "dresser_empty": False,
            "left_bookshelf_empty": False,
            "right_bookshelf_empty": False,
            "downstairs_table_empty": False,
            "downstairs_kitchen_empty": False,
            "downstairs_fireplace_empty": False,
            "basement_tools_empty": False,
            "dungeon_door_unlocked": False,
            "crypt_door_unlocked": False
        }