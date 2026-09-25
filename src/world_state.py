import pygame


class WorldState():
    def __init__(self):
        self.save_location = "farmhouse_bed"
        self.flags = {
            "basement_unlocked": False,
            "inventory_unlocked": False,
            "dresser_empty": False,
            "left_bookshelf_empty": False,
            "forbidden_book_taken": False,
            "combat_treatise_taken": False,
            "downstairs_boots_taken": False,
            "downstairs_table_empty": False,
            "downstairs_chest_empty": False,
            "downstairs_fireplace_empty": False,
            "basement_tools_taken": False,
            "basement_left_wall_checked": False,
            "basement_right_wall_checked": False,
            "basement_top_wall_checked": False,
            "basement_bottom_wall_checked": False,
            "basement_walls_broken": False,
            "basement_crate_empty": False,
            "basement_key_found": False,
            "basement_door_unlocked": False,
            "tunnel_1_empty": False,
            "tunnel_rope_placed": False,
            "tunnel_2_empty": False,
            "sewer_door_unlocked": False,
            "sewer_empty": False,
            "dungeon_door_unlocked": False,
            "dungeon_empty": False,
            "town_door_unlocked": False,
            "room_rented": False,
            "crypt_1_empty": False,
            "crypt_1_ritual_disrupted": False,
            "crypt_2_empty": False,
            "crypt_3_empty": False,
            "family_history_known": False,
            "amulet_known": False,
            "paladin_chest_looted": False,
            "reaper_knowledge": False,
            "lord_resolved": False,
            "reaper_choice_made": False,
            "accepted_deal": False,
            "lord_defeated": False,
            "reaper_reward_given": False
        }