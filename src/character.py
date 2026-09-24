import pygame
import math
from game_classes import GAME_CLASSES
from item_data import ITEMS, EQUIPMENT_TEMPLATES

stats = {
    "strength": 1,
    "dexterity": 1,
    "fortitude": 1,
    "faith": 1,
    "attunement": 1,
    "knowledge": 1
}

equipment_slots = {
    "head": None,
    "neck": None,
    "shirt": None,
    "torso": None,
    "hands": None,
    "arms": None,
    "waist": None,
    "pants": None,
    "leg armor": None,
    "feet": None,
    "shoes": None,
    "cloak": None,
    "ring": None,
    "bag": None,
    "main weapon": None,
    "secondary weapon": None
}


class Character:
    def __init__(self):
        self.stats = stats.copy()
        self.health = 100
        self.mana = 100
        self.level = 1
        self.experience = 0
        self.game_class = None
        self.power = 1
        self.buffs = []
        self.debuffs = []
        self.inventory = []
        self.coins = 0
        self.equipped = equipment_slots.copy()
        self.name = "Temp"

    # I made this a method for custom logic I am considering.
    def create(self, name, level: 1, game_class, inventory, coins, equipment):
        self.name = name
        self.level = level
        self.health += level * 5
        self.game_class = GAME_CLASSES[game_class]
        if inventory:
            self.inventory = inventory.copy()
        self.coins += coins
        if equipment:
            self.equipped = equipment.copy()


    def grant_exp(self, exp_gain):
        self.experience += exp_gain
        while self.experience >= self.exp_to_level(self.level + 1):
            self.level +=1


    def exp_to_level(self, level):
        return 50 * (level - 1) ** 2

    def set_class(self, game_class):
        if game_class not in GAME_CLASSES:
            raise ValueError("Incorrect class name.")
        self.game_class = GAME_CLASSES[game_class]
        if game_class == "Reaper" or game_class == "Paladin":
            self.equip_set(game_class)

    def equip_helper(self, new_item):
        new_item_data = ITEMS[new_item]
        item_slot = new_item_data["slot"]
        old_item = self.equipped[item_slot]
        if old_item is not None:
            self.inventory.append(old_item)
        self.equipped[item_slot] = new_item


    def equip_items(self, new_items):
        if isinstance(new_items, dict):
            for new_item in new_items.values():
                if new_item is not None:
                    self.equip_helper(new_item)
        elif isinstance(new_items, list):
            for new_item in new_items:
                self.equip_helper(new_item)
        elif isinstance(new_items, str):
            self.equip_helper(new_items)
        else:
            raise TypeError("Invalid argument for new_items.")

    def acquire_items(self, new_items):
        for item in new_items:
            if ITEMS[item]["slot"] is not None:
                self.auto_equip(item)
            else:
                self.inventory.append(item)
        # print("EQUIPPED AFTER LOOT:")
        # print(self.equipped)
        # print("INVENTORY AFTER LOOT:")
        # print(self.inventory)

    def auto_equip(self, new_item):
        new_item_data = ITEMS[new_item]
        item_slot = new_item_data["slot"]
        old_item = self.equipped[item_slot]
        if old_item is not None:
            old_item_data = ITEMS[old_item]
            if old_item_data["power"] < new_item_data["power"]:
                self.equip_helper(new_item)
            else:
                self.inventory.append(new_item)
        else:
            self.equip_helper(new_item)

    def equip_set(self, game_class):
        new_set = EQUIPMENT_TEMPLATES[game_class.lower()].copy()
        for new_item in new_set.values():
            if new_item is not None:
                self.equip_helper(new_item)

    def item_diminishing_returns(self, total):
        return 2 * math.sqrt(total)

    def equipment_power(self):
        total = 0
        for item in self.equipped.values():
            if item is not None:
                item_data = ITEMS[item]
                total += item_data["power"]
        return self.item_diminishing_returns(total)

    def check_class(self, game_class):
        if self.game_class == GAME_CLASSES[game_class]:
            return True
        return False

    def has_item(self, item):
        return item in self.inventory

    def exchange_item(self, item):
        count = 0
        if item == "Ancient Armament":
            while item in self.inventory:
                self.inventory.remove(item)
                count += 1
            self.power += count
        return count

    def to_dict(self):
        return {
            "stats": self.stats,
            "health": self.health,
            "mana": self.mana,
            "level": self.level,
            "exp": self.experience,
            "game_class": self.game_class.class_id,
            "power": self.power,
            "buffs": self.buffs,
            "debuffs": self.debuffs,
            "inventory": self.inventory,
            "coins": self.coins,
            "equipped": self.equipped,
            "name": self.name,
        }

    def apply_data(self, data):
        self.stats = data["player"]["stats"]
        self.health = data["player"]["health"]
        self.mana = data["player"]["mana"]
        self.level = data["player"]["level"]
        self.experience = data["player"]["exp"]
        game_class = data["player"]["game_class"]
        self.game_class = GAME_CLASSES[game_class]
        self.power = data["player"]["power"]
        self.buffs = data["player"]["buffs"]
        self.debuffs = data["player"]["debuffs"]
        self.inventory = data["player"]["inventory"]
        self.coins = data["player"]["coins"]
        self.equipped = data["player"]["equipped"]
        self.name = data["player"]["name"]