import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, MAP_HEIGHT



class Menu():
    def __init__(self, language_data):
        self.language_data = language_data
        self.options = {
            1: "Start Game",
            2: "Load Game",
            3: "Settings",
            4: "Exit"
        }
        self.settings = {
            1: "Change Language",
            2: "Toggle Hardcore",
            3: "Main Menu"
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
        title = title_font.render("Fantasy RPG", True, "Yellow")
        rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(title, rect)
        dialogue_rect = pygame.Rect(
        0,
        MAP_HEIGHT,
        SCREEN_WIDTH,
        SCREEN_HEIGHT - MAP_HEIGHT
        )
        for number, option in self.options.items():
            text = ui_font.render(f"{number}. {option}", True, "black")
            position = (
                dialogue_rect.x + 20,
                dialogue_rect.y + 20 + (number - 1) * 40
            )
            screen.blit(text, position)

    def draw_settings(self, screen, title_font, ui_font, settings):
        if settings["hardcore"] == True:
            difficulty = "Hardcore"
        else:
            difficulty = "Normal"
        language = settings["language"]
        title = title_font.render(f"Settings - Difficulty: {difficulty} Language: {language}", True, "Yellow")
        rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(title, rect)
        dialogue_rect = pygame.Rect(
        0,
        MAP_HEIGHT,
        SCREEN_WIDTH,
        SCREEN_HEIGHT - MAP_HEIGHT
        )
        for number, option in self.settings.items():
            text = ui_font.render(f"{number}. {option}", True, "black")
            position = (
                dialogue_rect.x + 20,
                dialogue_rect.y + 20 + (number - 1) * 40
            )
            screen.blit(text, position)
