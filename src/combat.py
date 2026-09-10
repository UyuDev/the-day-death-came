import pygame
import random


def combat_placeholder(player, enemy):
    if player.level == enemy.level:
        num = random.randint(1,100)
        if num > 95:
            return False
        else:
            return True
    elif player.level < enemy.level:
        num = random.randint(1,100)
        diff = enemy.level - player.level
        if num >= (90 - diff):
            return False
        else:
            return True
    else:
        return True

def calc_loot(enemy):
    loot = enemy.inventory.copy()
    coins = enemy.coins
    for item in enemy.equipped.values():
        if item is not None:
            loot.append(item)
    return loot, coins