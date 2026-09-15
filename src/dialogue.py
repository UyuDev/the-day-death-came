import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, MAP_HEIGHT
from dialogue_data import DIALOGUE



class Dialogue():
    def __init__(self, language_data, assets):
        self.current = "intro"
        self.language_data = language_data
        self.assets = assets
        self.ui = pygame.transform.scale(
            self.assets["ui_image"],
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        self.option_page = 0


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

    def has_options(self):
        current_node = DIALOGUE[self.current]
        if "options" in current_node:
            return True
        return False

    def set_current(self, node):
        self.current = node


    def advance(self, choice):
        current_node = DIALOGUE[self.current]
        if "options" in current_node:
            self.current = current_node["options"][choice]["next"]
        elif "next" in current_node:
            self.current = current_node["next"]


    def get_actions(self):
        current_node = DIALOGUE[self.current]
        if "actions" in current_node:
            actions = current_node["actions"]       
            return actions
        else:
            return []

    def draw(self, screen, ui_font):
        dialogue_rect = pygame.Rect(
        0,
        MAP_HEIGHT,
        SCREEN_WIDTH,
        SCREEN_HEIGHT - MAP_HEIGHT
        )
        current_node = DIALOGUE[self.current]
        if "options" in current_node:
            question_text = ui_font.render(self.language_data[current_node["text_id"]], True, "black")
            position = (
                dialogue_rect.x + 20,
                dialogue_rect.y + 20
            )
            screen.blit(self.ui, (0, 0))
            screen.blit(question_text, position)
            # options = list(current_node["options"].items())
            # if len(options) > 4:
            #     start = self.options_page * 3
            #     end = start + 3
            #     visible_options = options[start:end]
            #     for i in range(len(visible_options)):

            #         option_text = ui_font.render(f"{i+1}. {self.language_data[visible_options['text_id']]}", True, "black")
            #         position = (
            #             dialogue_rect.x + 20,
            #             dialogue_rect.y + 60 + (number - 1) * 40
            #         )
            #         screen.blit(option_text, position)
            #     if len(options) <= 6:
            #         start = self.options_page * 3
            #         end = start + 3
            #         visible_options = options[start:end]
                
            for number, option in current_node["options"].items():
                option_text = ui_font.render(f"{number}. {self.language_data[option['text_id']]}", True, "black")
                position = (
                    dialogue_rect.x + 20,
                    dialogue_rect.y + 60 + (number - 1) * 40
                )
                screen.blit(option_text, position)
        else:
            text = ui_font.render(self.language_data[current_node["text_id"]], True, "black")
            rect = text.get_rect(center=dialogue_rect.center)
            screen.blit(self.ui, (0, 0))
            screen.blit(text, rect)
        