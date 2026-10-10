import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, MAP_HEIGHT
from dialogue_data import DIALOGUE


TEXT_NODES = {
    "wip": {
        "text_id": "inventory.wip"
    },
    "summary": {
        "text_id": "inventory.summary",
        "variables": {},
        "options": {
            1: {
                "text_id": "inventory.option.view_items",
                "next": "view items"
            },
            2: {
                "text_id": "inventory.option.view_equipment",
                "next": "view equipment"
            },
            3: {
                "text_id": "inventory.empty",
                "next": "summary"
            },
            4: {
                "text_id": "inventory.empty",
                "next": "summary"
            }
        }
    },
}


class Inventory():
    def __init__(self, language_data, assets):
        self.current = "wip"
        self.variables = {}
        self.language_data = language_data
        self.assets = assets
        self.ui = pygame.transform.scale(
            self.assets["ui_image"],
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        self.inventory_index = 0
        self.equipped_index = 0
        self.text = None
        self.options = None
        self.nodes = []

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

    def handle_input_continue(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                return "Continue"
    # needs change
    def has_options(self):
        current_node = TEXT_NODES[self.current]
        if "options" in current_node:
            return True
        return False
    
    # needs change
    def set_current(self, node):
        self.current = node

    # unused
    def set_current_with_variables(self, node, variables):
        self.current = node
        self.variables = variables

    # needs change
    def advance(self, choice):
        current_node = TEXT_NODES[self.current]
        if "options" in current_node:
            self.current = current_node["options"][choice]["next"]
        elif "next" in current_node:
            self.current = current_node["next"]


    def display_stats(self, screen, ui_font, player):
        coins_text = self.language_data["stats.coins"]
        inventory_text = self.language_data["stats.inventory"]
        lvl_text = self.language_data["stats.level"]
        power_text = self.language_data["stats.power"]
        combined_text = f"{coins_text}: {player.coins}, {inventory_text}: {len(player.inventory)} / {player.capacity}, {lvl_text}: {player.level}, {power_text}: {player.total_power()}"
        text = ui_font.render(combined_text, True, "Yellow")
        screen.blit(text, (15, 15))

    def draw(self, screen, ui_font, player):
        dialogue_rect = pygame.Rect(
        0,
        MAP_HEIGHT,
        SCREEN_WIDTH,
        SCREEN_HEIGHT - MAP_HEIGHT
        )
        current_node = TEXT_NODES[self.current]
        if "options" in current_node:
            if "variables" in current_node:
                text_string = self.language_data[current_node["text_id"]].format(
                    **self.variables
                )
                question_text = ui_font.render(text_string, True, "black")
            else:
                question_text = ui_font.render(self.language_data[current_node["text_id"]], True, "black")
            
            position = (
                dialogue_rect.x + 20,
                dialogue_rect.y + 20
            )
            screen.blit(self.ui, (0, 0))
            screen.blit(question_text, position)
                
            for number, option in current_node["options"].items():
                option_text = ui_font.render(f"{number}. {self.language_data[option['text_id']]}", True, "black")
                position = (
                    dialogue_rect.x + 20,
                    dialogue_rect.y + 60 + (number - 1) * 40
                )
                screen.blit(option_text, position)

        else:
            if "variables" in current_node:
                text_string = self.language_data[current_node["text_id"]].format(
                    **self.variables
                )
            else:
                text_string = self.language_data[current_node["text_id"]]
            text = ui_font.render(text_string, True, "black")
            rect = text.get_rect(center=dialogue_rect.center)
            screen.blit(self.ui, (0, 0))
            screen.blit(text, rect)
        self.display_stats(screen, ui_font, player)       