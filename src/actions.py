import random
from save import can_save, save_game, reload_current_save

def handle_action(action, player, renderer, dialogue, world_state, save_menu, settings, exploration):
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
                handle_action(new_action, player, renderer, dialogue, world_state, save_menu, settings, exploration)
    elif action["type"] == "check_flag":
        if world_state.flags[action["target"]] == action["value"]:
            dialogue.set_current(action[f"if_pass"])
        else:
            dialogue.set_current(action[f"if_fail"])
        new_actions = dialogue.get_actions()
        for new_action in new_actions:
            handle_action(new_action, player, renderer, dialogue, world_state, save_menu, settings, exploration)
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
        result = exploration.explore_area(
            action["target"],
            player,
            world_state
        )
        if result == "death":
            reload_current_save(
                player,
                world_state,
                save_menu,
                renderer,
                dialogue
            )
            return "INTRO"

    elif action["type"] == "seek_enemies":
        result = exploration.seek_enemy(
            action["target"],
            player,
            world_state
        )
    elif action["type"] == "death":
        reload_current_save(
            player,
            world_state,
            save_menu,
            renderer,
            dialogue
        )
        return "INTRO"