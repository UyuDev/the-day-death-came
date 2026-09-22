import pygame
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
        self.flags = {}
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

    def equip_set(self, game_class):
        self.equipped = EQUIPMENT_TEMPLATES[game_class.lower()].copy()

    def check_class(self, game_class):
        if self.game_class == GAME_CLASSES[game_class]:
            return True
        return False