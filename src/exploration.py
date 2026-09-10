import pygame
from combat import combat_placeholder, calc_loot
from character import Character
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, MAP_HEIGHT
import random
from enemy_data import ENEMIES


TESTING = True
# I need the equivalent of dialogue nodes here
DIALOGUE = {}


ENCOUNTERS = {
    "door_encounter": {
        "enemies": ["farm_bandit", "farm_bandit", "farm_bandit", "farm_bandit"],
    },
    "tunnel_1_encounter": {
        "enemies": ["tunnel_bandit"],
    },
    "tunnel_1_enemies": {
        "enemies": ["tunnel_bandit", "tunnel_bandit", "tunnel_bandit"],
    }
}


class Exploration():
    def __init__(self, language_data):
        self.current = "intro"
        self.language_data = language_data
        self.area = None
        self.text = None
        self.options = None
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

    # can rework this is needed later
    # def has_options(self):
    #     current_node = DIALOGUE[self.current]
    #     if "options" in current_node:
    #         return True
    #     return False

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
            screen.blit(text, rect)


    def explore_encounter(self):
        num = random.randint(1,5)
        if num == 5:
            return True
        return False

    def explore_area(self, target, player):
        encounter = self.explore_encounter()
        if encounter:
            result = self.seek_enemy(target, player)
            if result == "death":
                return "death"
        num = random.randint(1,5)
        #temp
        player.coins += num
        if num == 1:
            print(f"You receive 1 coin.")
        else:
            print(f"You receive {num} coins.")

    def seek_enemy_old(self, encounter_data, player):
        if not isinstance(encounter_data, Character):
            enemy = Character()
            # name, level: 1, game_class, inventory, equipment
            enemy_type = ENEMIES[encounter_data]
            enemy.create(enemy_type["name"], enemy_type["level"], enemy_type["game_class"], enemy_type["inventory"], enemy_type["coins"], enemy_type["equipment"])
        else:
            enemy = encounter_data
            print("Update the encounter function before release")
        print(f"You encounter: {enemy}.")
        if combat_placeholder(player, enemy) == False:
            return "death"
        else:
            print(f"You defeated {enemy.name}")
            if TESTING:
                player.level += 1
                print(f"You have reached level {player.level}.")
            else:
                player.grant_exp(10)
                print(f"You gain 10 experience.")
            loot, coins = calc_loot(enemy)
            print(f"You receive loot: {loot}.")
            if coins != 0:
                player.coins += coins
                if coins == 1:
                    print(f"You receive 1 coin.")
                else:
                    print(f"You receive {coins} coins.")
            return "win"


    def seek_enemy(self, encounter_data, player):
        enemies = []
        if not isinstance(encounter_data, Character):
            for enemy_unit in ENCOUNTERS[encounter_data]["enemies"]:
                enemy = Character()
                # name, level: 1, game_class, inventory, equipment
                enemy_type = ENEMIES[enemy_unit]
                enemy.create(enemy_type["name"], enemy_type["level"], enemy_type["game_class"], enemy_type["inventory"], enemy_type["coins"], enemy_type["equipped"])
                enemies.append(enemy)
        #in case the enemy is being passed for some reason
        else:
            enemy = encounter_data
            print("Update the encounter function before release")
        for enemy in enemies:
            print(f"You encounter: {enemy.name}.")
            if combat_placeholder(player, enemy) == False:
                return "death"
            else:
                print(f"You defeated {enemy.name}")
                if TESTING:
                    player.level += 1
                    print(f"You have reached level {player.level}.")
                else:
                    player.grant_exp(10)
                    print(f"You gain 10 experience.")
                loot, coins = calc_loot(enemy)
                print(f"You receive loot: {loot}.")
                if coins != 0:
                    player.coins += coins
                    if coins == 1:
                        print(f"You receive 1 coin.")
                    else:
                        print(f"You receive {coins} coins.")
                        return "win"
                return "win"



    def encounter(self, encounter_data, player):
        enemies = []
        if not isinstance(encounter_data, Character):
            for enemy_unit in ENCOUNTERS[encounter_data]["enemies"]:
                enemy = Character()
                # name, level: 1, game_class, inventory, equipment
                enemy_type = ENEMIES[enemy_unit]
                enemy.create(enemy_type["name"], enemy_type["level"], enemy_type["game_class"], enemy_type["inventory"], enemy_type["coins"], enemy_type["equipped"])
                enemies.append(enemy)
        #in case the enemy is being passed for some reason
        else:
            enemy = encounter_data
            print("Update the encounter function before release")
        for enemy in enemies:
            print(f"You encounter: {enemy.name}.")
            if combat_placeholder(player, enemy) == False:
                return "death"
            else:
                print(f"You defeated {enemy.name}")
                if TESTING:
                    player.level += 1
                    print(f"You have reached level {player.level}.")
                else:
                    player.grant_exp(10)
                    print(f"You gain 10 experience.")
                loot, coins = calc_loot(enemy)
                print(f"You receive loot: {loot}.")
                if coins != 0:
                    player.coins += coins
                    if coins == 1:
                        print(f"You receive 1 coin.")
                    else:
                        print(f"You receive {coins} coins.")
                        return "win"
                return "win"
