import pygame



def combat_placeholder(player, enemy):
    if player.level < enemy.level:
        return False
    return True

def calc_loot(enemy):
    loot = enemy.inventory.copy()
    for item in enemy.equipped.values():
        if item is not None:
            loot.append(enemy.equipped[item])
    return loot