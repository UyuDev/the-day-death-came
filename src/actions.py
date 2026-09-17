import random
from save import can_save, save_game, reload_current_save

def handle_action(action, player, renderer, dialogue, world_state, save_menu, settings, exploration):
    if action["type"] == "encounter":
        if action["target"] == "door_encounter":
            if player.level < 10:
                number = random.randint(1, 4)
                dialogue.set_current(action["on_loss"] + f" {number}")
            else:
                # later implement the combat
                result = exploration.simulate_encounter(action["target"], player)
                if result == "death":
                    reload_current_save(
                        player,
                        world_state,
                        save_menu,
                        renderer,
                        dialogue
                    )
                    return "INTRO"
                dialogue.set_current(action["on_win"])
            new_actions = dialogue.get_actions()
            for new_action in new_actions:
                result = handle_action(new_action, player, renderer, dialogue, world_state, save_menu, settings, exploration)
                if result is not None:
                    return result
        else:
            exploration.start_encounter(action["target"], player)
            return "EXPLORATION"
    elif action["type"] == "check_flag":
        if world_state.flags[action["target"]] == action["value"]:
            dialogue.set_current(action[f"if_pass"])
        else:
            dialogue.set_current(action[f"if_fail"])
        new_actions = dialogue.get_actions()
        for new_action in new_actions:
            result = handle_action(new_action, player, renderer, dialogue, world_state, save_menu, settings, exploration)
            if result is not None:
                return result
    elif action["type"] == "map":
        renderer.load_map(action["target"])
    elif action["type"] == "set_flag":
        world_state.flags[action["target"]] = action["value"]
    elif action["type"] == "item":
        player.inventory.extend([action["target"]] * action["value"])
    elif action["type"] == "equip":
        player.equipped[action["slot"]] = action["target"]
    elif action["type"] == "restore_health":
        if action["target"] == "full":
            player.health = 100
    elif action["type"] == "main_menu":
        return "MENU"
    elif action["type"] == "show_scene":
        renderer.show_scene(action["target"])
    elif action["type"] == "clear_scene":
        renderer.clear_scene()
    elif action["type"] == "save_game":
        if can_save(settings, player):
            save_game(
                player,
                world_state.flags,
                world_state.save_location,
                save_menu.current_slot
            )
    elif action["type"] == "explore_items":
        exploration.start_loot_search(
            action["target"],
            player
        )
        return "EXPLORATION"
    elif action["type"] == "death":
        reload_current_save(
            player,
            world_state,
            save_menu,
            renderer,
            dialogue
        )
        return "INTRO"
    elif action["type"] == "exit_exploration":
        return "INTRO"