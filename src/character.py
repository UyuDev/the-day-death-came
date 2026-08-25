import pygame


class Character:
    def __init__(self):
        self.flags = {}
        self.health = 100
        self.mana = 100
        self.level = 1
        self.experience = 0
        self.game_class = None
        self.buffs = []
        self.debuffs = []
        self.inventory = []