import json

#should be fine
def load_save(slot):
    with open(f"saves/save_{slot}.json", "r") as file:
        return json.load(file)

def can_save(settings, player):
    if settings["hardcore"] == False:
        if "Insomnia" in player.debuffs:
            return False
        return True
    return True

def save_game(player, flags, save_location, slot):
    save_data = {
        "save_name": f"Nicholas - {save_location} - Level {player.level}",
        "player": {
            "level": player.level,
            "inventory": player.inventory,
            "equipment": player.equipment,
        },
        "save_location": save_location,
        "flags": flags
    }

    with open(f"saves/save_{slot}.json", "w") as file:
        json.dump(save_data, file, indent=4)

# WIP
def apply_save(save):
    return