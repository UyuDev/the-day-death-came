import pygame
import random


def combat_placeholder(player, enemy):
    base = 95
    bonus = (player.level * 7) + player.power + (player.game_class.power * 0.5)
    reduction = (enemy.level * 7) + enemy.power + (enemy.game_class.power * 0.5)
    final_chance = base + bonus - reduction
    final_chance = max(5, min(100, final_chance))
    num = random.randint(1,100)
    print(f"{enemy.name} combat stats:\nbonus: {bonus}, reduction: {reduction}, final_chance: {final_chance}\nroll: {num}")
    print(
    f"{enemy.name} combat stats:\n"
    f"player class: {player.game_class.name_id}\n"
    f"player level: {player.level}\n"
    f"player power: {player.power}\n"
    f"class power: {player.game_class.power}\n"
    f"bonus: {bonus}\n"
    f"reduction: {reduction}\n"
    f"final_chance: {final_chance}\n"
    f"roll: {num}"
    )
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