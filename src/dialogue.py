import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, MAP_HEIGHT
from dialogue_data import DIALOGUE



class Dialogue():
    def __init__(self):
        self.current = "intro"


    def handle_input(self, event):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    return "Continue"
                elif event.key == pygame.K_1:
                    print(pygame.K_1)
                    return 1
                elif event.key == pygame.K_2:
                    return 2
                elif event.key == pygame.K_3:
                    return 3
                elif event.key == pygame.K_4:
                    return 4
                elif event.key == pygame.K_5:
                    return 5
                elif event.key == pygame.K_6:
                    return 6

    def advance(self, choice):
        current_node = DIALOGUE[self.current]
        # if self.current == "You died.":
        #     self.current = "intro"
        if "options" in current_node:
            self.current = current_node["options"][choice]["next"]
        elif "map" in current_node:
            self.current = current_node["next"]
            return current_node["map"]
        else:
            self.current = current_node["next"]

    def draw(self, screen, ui_font):
        dialogue_rect = pygame.Rect(
        0,
        MAP_HEIGHT,
        SCREEN_WIDTH,
        SCREEN_HEIGHT - MAP_HEIGHT
        )
        current_node = DIALOGUE[self.current]
        if "options" in current_node:
            question_text = ui_font.render(current_node["text"], True, "black")
            position = (
                dialogue_rect.x + 20,
                dialogue_rect.y + 20
            )
            screen.blit(question_text, position)
            for number, option in current_node["options"].items():
                option_text = ui_font.render(f"{number}. {option['text']}", True, "black")
                position = (
                    dialogue_rect.x + 20,
                    dialogue_rect.y + 60 + (number - 1) * 40
                )
                screen.blit(option_text, position)
        else:
            text = ui_font.render(current_node["text"], True, "black")
            rect = text.get_rect(center=dialogue_rect.center)
            screen.blit(text, rect)
        