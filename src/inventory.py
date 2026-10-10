import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, MAP_HEIGHT
from dialogue_data import DIALOGUE


TEXT_NODES = {
    "wip": {
        "text_id": "inventory.wip"
    },
    "empty inventory": {
        "text_id": "inventory.empty_inventory"
    },
    "summary": {
        "text_id": "inventory.summary",
        "variables": {},
        "options": {
            1: {
                "text_id": "inventory.option.view_items"
            },
            2: {
                "text_id": "inventory.option.view_equipment"
            },
            3: {
                "text_id": "inventory.option.empty"
            },
            4: {
                "text_id": "inventory.option.empty"
            }
        }
    },
    "items": {
        "text_id": "inventory.items",
        "variables": {},
        "options": {
            1: {
                "text_id": "inventory.option.next_item"
            },
            2: {
                "text_id": "inventory.option.empty"
            },
            3: {
                "text_id": "inventory.option.summary"
            },
            4: {
                "text_id": "inventory.option.previous_item"
            }
        }
    },
    "equipment": {
        "text_id": "inventory.equipment",
        "variables": {},
        "options": {
            1: {
                "text_id": "inventory.option.next_slot"
            },
            2: {
                "text_id": "inventory.option.empty"
            },
            3: {
                "text_id": "inventory.option.summary"
            },
            4: {
                "text_id": "inventory.option.previous_slot"
            }
        }
    }
}


class Inventory():
    def __init__(self, language_data, assets):
        self.current = "summary"
        self.summary_variables = {}
        self.language_data = language_data
        self.assets = assets
        self.ui = pygame.transform.scale(
            self.assets["ui_image"],
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        self.items = []
        self.equipment = []
        self.item_index = 0
        self.equipment_index = 0

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
                
    # leaving this for later
    def handle_input_continue(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                return "Continue"
            

    def prepare_data(self, player):
        self.item_index = 0
        self.equipment_index = 0
        self.current = "summary"
        self.items = player.inventory_data()
        self.equipment = player.equipment_data()
        self.summary_variables = {"unique_items": len(self.items), "equipped_power": player.raw_equipment_power(), "empty_slots": player.calc_empty_slots()}


    # might as well leave this for later
    def has_options(self):
        current_node = TEXT_NODES[self.current]
        if "options" in current_node:
            return True
        return False
    
    # unused
    def set_current(self, node):
        self.current = node

    # unused
    def set_current_with_variables(self, node, variables):
        self.current = node
        self.variables = variables

    # wip
    def advance(self, choice):
        if self.current == "summary":
            if choice == 1:
                self.current = "items"
            elif choice == 2:
                self.current = "equipment"
        elif self.current == "items":
            if choice == 1:
                if len(self.items) > 0:
                    self.item_index = (self.item_index + 1) % len(self.items)
            elif choice == 2:
                print("Dropping items is not yet implemented.")
            elif choice == 3:
                self.current = "summary"
            elif choice == 4:
                if len(self.items) > 0:
                    self.item_index = (self.item_index - 1) % len(self.items)
        elif self.current == "equipment":
            if choice == 1:
                self.equipment_index = (self.equipment_index + 1) % len(self.equipment)
            elif choice == 2:
                print("Unequiping items is not yet implemented.")
            elif choice == 3:
                self.current = "summary"
            elif choice == 4:
                self.equipment_index = (self.equipment_index - 1) % len(self.equipment)



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

                if self.current == "summary":
                    text_string = self.language_data[current_node["text_id"]].format(
                        **self.summary_variables
                    )
                    question_text = ui_font.render(text_string, True, "black")

                elif self.current == "items":
                    if len(self.items) == 0:
                        text_string = self.language_data[TEXT_NODES["empty inventory"]["text_id"]]
                    else:
                        name_id, count, is_sellable, value, total_value = self.items[self.item_index]
                        variables = {
                            "name": self.language_data[name_id],
                            "count": count,
                            "sellable": self.language_data[is_sellable],
                            "value": value,
                            "total_value": total_value
                        }
                        text_string = self.language_data[current_node["text_id"]].format(
                            **variables
                        )
                    question_text = ui_font.render(text_string, True, "black")  

                elif self.current == "equipment":
                    slot_name, name_id, power = self.equipment[self.equipment_index]
                    variables = { 
                        "slot": self.language_data[slot_name],
                        "name": self.language_data[name_id],
                        "power": power
                    }                    
                    text_string = self.language_data[current_node["text_id"]].format(
                        **variables
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

        else: # unused for now
            if "variables" in current_node:
                text_string = self.language_data[current_node["text_id"]].format(
                    **variables
                )
            else:
                text_string = self.language_data[current_node["text_id"]]
            text = ui_font.render(text_string, True, "black")
            rect = text.get_rect(center=dialogue_rect.center)
            screen.blit(self.ui, (0, 0))
            screen.blit(text, rect)
        self.display_stats(screen, ui_font, player)       