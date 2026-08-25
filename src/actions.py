import random


def handle_action(action, player, grid, dialogue):
    if action["type"] == "combat":
        if action["target"] == "door_encounter":
            if player.level < 5:
                number = random.randint(1, 4)
                dialogue.set_current(action[f"on_loss"] + f" {number}")
            else:
                # later implement the combat
                dialogue.set_current(action["on_win"])
    elif action["type"] == "map":
        grid.load_map(action["target"])
    elif action["type"] == "set_flag":
        player.flags[action["target"]] = action["value"]
    return