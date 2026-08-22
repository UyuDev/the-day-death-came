import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, MAP_HEIGHT



class Menu():
    def __init__(self, language_data):
        self.language_data = language_data
        self.options = {
            1: "menu.start_game",
            2: "menu.load_game",
            3: "menu.settings",
            4: "menu.exit"
        }
        self.settings = {
            1: "settings.change_language",
            2: "settings.toggle_hardcore",
            3: "settings.main_menu"
        }


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

    def draw(self, screen, title_font, ui_font):
        title_text = self.language_data["menu.title"]
        title = title_font.render(title_text, True, "Yellow")
        rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(title, rect)
        dialogue_rect = pygame.Rect(
        0,
        MAP_HEIGHT,
        SCREEN_WIDTH,
        SCREEN_HEIGHT - MAP_HEIGHT
        )
        for number, option in self.options.items():
            text = ui_font.render(f"{number}. {self.language_data[option]}", True, "black")
            position = (
                dialogue_rect.x + 20,
                dialogue_rect.y + 20 + (number - 1) * 40
            )
            screen.blit(text, position)

    def draw_settings(self, screen, title_font, ui_font, settings):
        if settings["hardcore"]:
            difficulty = self.language_data["settings.difficulty_hard"]
        else:
            difficulty = self.language_data["settings.difficulty_normal"]
        language = settings["language"]
        text_1 = self.language_data["settings.part_1"]
        text_2 = self.language_data["settings.part_2"]
        title = title_font.render(f"{text_1}{difficulty}{text_2}{language}", True, "Yellow")
        rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(title, rect)
        dialogue_rect = pygame.Rect(
        0,
        MAP_HEIGHT,
        SCREEN_WIDTH,
        SCREEN_HEIGHT - MAP_HEIGHT
        )
        for number, option in self.settings.items():
            text = ui_font.render(f"{number}. {self.language_data[option]}", True, "black")
            position = (
                dialogue_rect.x + 20,
                dialogue_rect.y + 20 + (number - 1) * 40
            )
            screen.blit(text, position)
