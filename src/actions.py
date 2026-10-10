import random
from save import can_save, save_game, reload_current_save

def handle_action(action, player, renderer, dialogue, world_state, save_menu, settings, exploration):
    if action["type"] == "encounter":
        if action["target"] == "door_encounter" and player.level < 10:
                number = random.randint(1, 4)
                dialogue.set_current(f"door death {number}")
                new_actions = dialogue.get_actions()
                for new_action in new_actions:
                    result = handle_action(new_action, player, renderer, dialogue, world_state, save_menu, settings, exploration)
                    if result is not None:
                        return result
        # simplified logic
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
        player.acquire_items([action["target"]] * action["value"])

    elif action["type"] == "equip":
        player.equip_items(action["target"])

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
            world_state.save_location = action["target"]
            save_game(
                player,
                world_state.flags,
                world_state.save_location,
                save_menu.current_slot,
                dialogue.language_data
            )

    elif action["type"] == "explore_items":
        exploration.start_loot_search(
            action["target"],
            player
        )
        return "EXPLORATION"
    
    elif action["type"] == "death":
        front_door_encountered = world_state.flags["front_door_encountered"]
        if settings["hardcore"]:
            return "HARDCORE_DEATH"
        reload_current_save(
            player,
            world_state,
            save_menu,
            renderer,
            dialogue
        )
        world_state.flags["has_died"] = True
        if front_door_encountered:
            world_state.flags["front_door_encountered"] = True
        return "DIALOGUE"
    
    elif action["type"] == "exit_exploration":
        return "DIALOGUE"
    
    elif action["type"] == "set_class":
        player.set_class(action["target"])

    elif action["type"] == "check_class":         
        if player.check_class(action["target"]):
            dialogue.set_current(action["if_pass"])
        else:
            dialogue.set_current(action["if_fail"])
        new_actions = dialogue.get_actions()
        for new_action in new_actions:
            result = handle_action(new_action, player, renderer, dialogue, world_state, save_menu, settings, exploration)
            if result is not None:
                return result
            
    elif action["type"] == "sell_items":         
        if action["target"] == "black_market_fence":
            result = player.fence_items()
            if result is None:
                dialogue.set_current(action["if_fail"])
            else:
                total_count, total_coins = result
                dialogue.set_current_with_variables(action["if_pass"], {"total_count": total_count, "total_coins": total_coins})

            # WIP - check amount
    elif action["type"] == "check_items":
        print("Current node:", dialogue.current, "Action:", action)      
        if player.has_item(action["target"], action["value"]):
            dialogue.set_current(action["if_pass"])
        else:
            dialogue.set_current(action["if_fail"])
        new_actions = dialogue.get_actions()
        for new_action in new_actions:
            result = handle_action(new_action, player, renderer, dialogue, world_state, save_menu, settings, exploration)
            if result is not None:
                return result
            
            # WIP - craft item
    elif action["type"] == "exchange_power":    
        print("Current node:", dialogue.current, "Action:", action)     
        if action["target"] == "Ancient Armament" or action["target"] == "Crystal Fragment":
            count, power = player.exchange_power(action["target"])
            dialogue.set_current_with_variables(action["next"], {"count": count, "power": power})
        elif action["target"] == "Rare Potion" or action["target"] == "Strange Potion" or action["target"] == "Bones":
            player.exchange_power(action["target"])
            dialogue.set_current(action["next"])
        else:
            player.exchange_item(action["target"])
            dialogue.set_current(action["next"])    

    elif action["type"] == "exchange_armament":    
        print("Current node:", dialogue.current, "Action:", action)     
        player.exchange_item(action["target"]) 

    elif action["type"] == "earn_coins":
        player.coins += action["value"]

    elif action["type"] == "check_coins":
        print("Current node:", dialogue.current, "Action:", action)           
        if player.has_coins(action["value"]):
            dialogue.set_current(action["if_pass"])
        else:
            dialogue.set_current(action["if_fail"])
        new_actions = dialogue.get_actions()
        for new_action in new_actions:
            result = handle_action(new_action, player, renderer, dialogue, world_state, save_menu, settings, exploration)
            if result is not None:
                return result

    elif action["type"] == "spend_coins":         
        if player.has_coins(action["value"]):
            player.spend_coins(action["value"])

    elif action["type"] == "check_settings":
        if settings[action["target"]]:
            dialogue.set_current(action["if_pass"])
        else:
            dialogue.set_current(action["if_fail"])
        new_actions = dialogue.get_actions()
        for new_action in new_actions:
            result = handle_action(new_action, player, renderer, dialogue, world_state, save_menu, settings, exploration)
            if result is not None:
                return result
    elif action["type"] == "check_level":
        return player.level >= action["target"]