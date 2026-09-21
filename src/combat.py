import pygame
import random


def combat_placeholder(player, enemy):
    base = 80
    bonus = player.level + player.power + player.game_class.power
    reduction = enemy.level + enemy.power + enemy.game_class.power
    final_chance = base + bonus - reduction
    num = random.randint(1,100)
    print(f"{enemy.name} combat stats:\nbonus: {bonus}, reduction: {reduction}, final_chance: {final_chance}\nroll: {num}")
    if final_chance < num:
        return False
    return True


def calc_loot(enemy):
    loot = enemy.inventory.copy()
    coins = enemy.coins
    for item in enemy.equipped.values():
        if item is not None:
            loot.append(item)
    return loot, coins