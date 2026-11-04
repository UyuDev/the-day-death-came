import json
import pygame
from pathlib import Path
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, MAP_HEIGHT

#should be fine
def load_save(slot):
    path = Path(f"saves/save_{slot}.json")

    if not path.exists():
        return None

    with open(path, "r") as file:
        return json.load(file)

def can_save(settings, player):
    if settings["hardcore"] == True:
        if "Insomnia" in player.debuffs:
            return False
        return True
    return True

def save_game(player, flags, save_location, slot, language_data):
    Path("saves").mkdir(exist_ok=True)

    player_data = player.to_dict()
    save_data = {
        "save_name": f"{language_data[player.name]} - {language_data[SAVE_LOCATIONS[save_location]["name_id"]]} - {language_data["save.level"]} {player.level}",
        "player": player_data,
        "save_location": save_location,
        "flags": flags
    }

    with open(f"saves/save_{slot}.json", "w") as file:
        json.dump(save_data, file, indent=4)

# WIP
def apply_save(data, player, world_state):
    player.apply_data(data)
    world_state.flags = data["flags"]
    world_state.save_location = data["save_location"]

SAVE_LOCATIONS = {
    "farmhouse_bed": {
        "map": "house_upstairs",
        "name_id": "save.upstairs_bed",
        "dialogue": "intro wake",
        "death_dialogue": "farmhouse death wake"
    },
    "inn_bed": {
        "map": "town",
        "name_id": "save.inn_bed",
        "dialogue": "inn wake",
        "death_dialogue": "inn death wake"
    }
}

def reload_current_save(player, world_state, save_menu, renderer, dialogue, died=False):
    save_data = load_save(save_menu.current_slot)

    if save_data is None:
        return False

    apply_save(save_data, player, world_state)

    checkpoint = SAVE_LOCATIONS[world_state.save_location]
    renderer.load_map(checkpoint["map"])

    dialogue_key = "death_dialogue" if died else "dialogue"
    dialogue.set_current(checkpoint[dialogue_key])

    player.health = 100
    return True


class SaveMenu():
    def __init__(self, language_data, assets):
        self.language_data = language_data
        self.assets = assets
        self.page = 1
        self.current = None
        self.current_slot = 1
        self.menu_art = pygame.transform.scale(
            self.assets["menuscreen_art"],
            (SCREEN_WIDTH, MAP_HEIGHT)
        )
        self.ui = pygame.transform.scale(
            self.assets["ui_image"],
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        self.options_1 = {
            1: "save_menu.load_1",
            2: "save_menu.load_2",
            3: "save_menu.more_options",
            4: "save_menu.return"
        }
        self.options_2 = {
            1: "save_menu.load_3",
            2: "save_menu.load_4",
            3: "save_menu.previous_options",
            4: "save_menu.return"
        }


    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                return 1
            elif event.key == pygame.K_2:
                return 2
            elif event.key == pygame.K_3:
                return 3
            elif event.key == pygame.K_4:
                return 4
            elif event.key == pygame.K_RETURN:
                if self.current is None:
                    return "new_game"
                else:
                    return "load_game"
    # unused
    def draw(self, screen, title_font, ui_font):
        title_text = self.language_data["menu.title"]
        title = title_font.render(title_text, True, "Yellow")
        rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(self.menu_art, (0, 0))
        screen.blit(self.ui, (0, 0))
        screen.blit(title, rect)
        dialogue_rect = pygame.Rect(
        0,
        MAP_HEIGHT,
        SCREEN_WIDTH,
        SCREEN_HEIGHT - MAP_HEIGHT
        )
        if self.page == 1:
            options = self.options_1
        else:
            options = self.options_2
        for number, option in options.items():
            text = ui_font.render(f"{number}. {self.language_data[option]}", True, "black")
            position = (
                dialogue_rect.x + 20,
                dialogue_rect.y + 20 + (number - 1) * 40
            )
            screen.blit(text, position)


    def change_page(self):
        if self.page == 1:
            self.page = 2
        else:
            self.page = 1

    def set_current(self, save):
        self.current = save

    def draw_options(self, screen, title_font, ui_font):
        if self.current is None:
            text = self.language_data["save_menu.new_save"]
            hint_text = self.language_data["save_menu.press_enter_new"]
        else:
            text = self.current["save_name"]
            hint_text = self.language_data["save_menu.press_enter_load"]
        screen.blit(self.menu_art, (0, 0))
        screen.blit(self.ui, (0, 0))
        title = title_font.render(f"{text}", True, "Yellow")
        rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(title, rect)
        hint = ui_font.render(f"{hint_text}", True, "Yellow")
        hint_rect = hint.get_rect(center=(SCREEN_WIDTH // 2, 150))
        screen.blit(hint, hint_rect)
        dialogue_rect = pygame.Rect(
        0,
        MAP_HEIGHT,
        SCREEN_WIDTH,
        SCREEN_HEIGHT - MAP_HEIGHT
        )
        if self.page == 1:
            options = self.options_1
        else:
            options = self.options_2
        for number, option in options.items():
            text = ui_font.render(f"{number}. {self.language_data[option]}", True, "black")
            position = (
                dialogue_rect.x + 20,
                dialogue_rect.y + 20 + (number - 1) * 40
            )
            screen.blit(text, position)