import random


def handle_action(action, player, renderer, dialogue, world_state):
    if action["type"] == "combat":
        if action["target"] == "door_encounter":
            if player.level < 5:
                number = random.randint(1, 4)
                dialogue.set_current(action[f"on_loss"] + f" {number}")
            else:
                # later implement the combat
                dialogue.set_current(action["on_win"])
            new_actions = dialogue.get_actions()
            for new_action in new_actions:
                handle_action(new_action, player, renderer, dialogue, world_state)
    elif action["type"] == "check_flag":
        if world_state.flags[action["target"]] == action["value"]:
            dialogue.set_current(action[f"if_pass"])
        else:
            dialogue.set_current(action[f"if_fail"])
        new_actions = dialogue.get_actions()
        for new_action in new_actions:
            handle_action(new_action, player, renderer, dialogue, world_state)
    elif action["type"] == "map":
        renderer.load_map(action["target"])
    elif action["type"] == "set_flag":
        world_state.flags[action["target"]] = action["value"]
    elif action["type"] == "item":
        player.inventory.extend([action["target"]] * action["value"])
    elif action["type"] == "show_scene":
        renderer.show_scene(action["target"])
    elif action["type"] == "clear_scene":
        renderer.clear_scene()
    
    return