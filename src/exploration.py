import pygame
from combat import combat_placeholder, calc_loot
from character import Character
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, MAP_HEIGHT
import random
from enemy_data import ENEMIES


TESTING = False

TEXT_NODES = {
    "engage": {
        "text_id": "exploration.combat_engage"
    },
    "win": {
        "text_id": "exploration.win"
    },
    "loss": {
        "text_id": "exploration.loss"
    },
    "xp": {
        "text_id": "exploration.xp"
    },
    "loot": {
        "text_id": "exploration.loot"
    },
    "search": {
        "text_id": "exploration.search"
    },
    "search_success": {
        "text_id": "exploration.search_success"
    },
    "search_interrupted": {
        "text_id": "exploration.search_interrupted"
    },
}

ENCOUNTERS = {
    "door_encounter": {
        "enemies": ["farm_bandit", "farm_bandit", "farm_bandit", "farm_bandit"],
        "text_id": "exploration.door_encounter"
    },
    "tunnel_1_encounter": {
        "enemies": ["tunnel_bandit"],
        "text_id": "exploration.tunnel_1_encounter"
    },
    "tunnel_1": {
        "enemies": ["giant_rat", "giant_rat", "giant_rat"],
        "text_id": "exploration.tunnel_1_enemies"
    },
    "tunnel_2": {
        "enemies": ["cave_goblin", "cave_goblin", "cave_goblin", "cave_goblin"],
        "text_id": "exploration.tunnel_2_enemies"
    },
    "sewer": {
        "enemies": ["sewer_bandit", "sewer_bandit", "sewer_bandit", "sewer_bandit", "sewer_bandit"],
        "text_id": "exploration.sewer_enemies"
    },
    "dungeon": {
        "enemies": ["dungeon_bandit", "dungeon_bandit", "dungeon_bandit", "dungeon_bandit", "dungeon_bandit", "dungeon_bandit"],
        "text_id": "exploration.dungeon_enemies"
    },
    "crypt_1_enemies_1": {
        "enemies": ["skeleton", "skeleton", "zombie", "zombie"],
        "text_id": "exploration.crypt_1_enemies_1"
    },
    "crypt_1_enemies_2": {
        "enemies": ["skeleton_fighter", "cultist_acolyte", "skeleton_fighter", "cultist_acolyte"],
        "text_id": "exploration.crypt_1_enemies_2"
    },
    "crypt_2_enemies_1": {
        "enemies": ["skeleton_warrior", "skeleton_mage", "skeleton_warrior", "skeleton_mage"],
        "text_id": "exploration.crypt_2_enemies_1"
    },
    "crypt_2_enemies_2": {
        "enemies": ["skeleton_knight", "skeleton_darkmaster", "skeleton_knight", "skeleton_darkmaster"],
        "text_id": "exploration.crypt_2_enemies_2"
    },
    "crypt_3_enemies_1": {
        "enemies": ["honor_guard", "honor_guard", "honor_guard", "honor_guard"],
        "text_id": "exploration.crypt_3_enemies_1"
    },
    "crypt_3_enemies_2": {
        "enemies": ["lord_graye", "honor_guard", "honor_guard"],
        "text_id": "exploration.crypt_3_enemies_2"
    },
    "crypt_3_boss_1": {
        "enemies": ["reaper_boss_1"],
        "text_id": "exploration.crypt_3_boss_1"
    },
    "crypt_3_boss_2": {
        "enemies": ["reaper_boss_2"],
        "text_id": "exploration.crypt_3_boss_2"
    },
    "crypt_3_boss_3": {
        "enemies": ["reaper_boss_3"],
        "text_id": "exploration.crypt_3_boss_3"
    },
    "crypt_3_boss_4": {
        "enemies": ["reaper_boss_4"],
        "text_id": "exploration.crypt_3_boss_4"
    }
}

SEARCH_AREAS = {
    "tunnel_1": {
        "containers": [
            {
                "type": "chest",
                "loot": ["Leather Gloves"],
                "coins": 5
            }
        ],
        "text_id": "exploration.tunnel_1_loot"
    },
    "tunnel_2": {
        "containers": [
            {
                "type": "crate",
                "loot": ["Strange Herb"],
                "coins": 0
            },
            {
                "type": "chest",
                "loot": ["Gambeson"],
                "coins": 5
            }
        ],
        "text_id": "exploration.tunnel_2_loot"
    },
    "sewer": {
        "containers": [
            {
                "type": "crates",
                "loot": ["Strange Herb", "Alchemy Kit"],
                "coins": 0
            },
            {
                "type": "chest",
                "loot": ["Longsword"],
                "coins": 5
            }
        ],
        "text_id": "exploration.sewer_loot"
    },
    "dungeon": {
        "containers": [
            {
                "type": "crates",
                "loot": ["Strange Herb", "Rare Ingredient"],
                "coins": 0
            },
            {
                "type": "chest",
                "loot": ["Chainmail Hauberk"],
                "coins": 8
            }
        ],
        "text_id": "exploration.dungeon_loot"
    },
    "crypt_1": {
        "containers": [
            {
                "type": "Tomb",
                "loot": ["Old Journal Page"],
                "coins": 0
            }
        ],
        "text_id": "exploration.crypt_1_loot"
    },
    "crypt_2": {
        "containers": [
            {
                "type": "Tomb",
                "loot": ["Old Necklace"],
                "coins": 0
            }
        ],
        "text_id": "exploration.crypt_2_loot"
    },
    "crypt_3": {
        "containers": [
            {
                "type": "Small Chest",
                "loot": ["Shiny Key"],
                "coins": 0
            }
        ],
        "text_id": "exploration.crypt_3_loot"
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
        self.nodes = []
        self.current_index = 0
        self.result = None



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


    def set_current(self, node):
        self.current = node


    def advance(self, choice):
        if choice == "Continue":
            self.current_index += 1
            if self.current_index >= len(self.sequence):
                if self.result == "death":
                    return "death"
                return "continue"


    def get_actions(self):
        return []

    def draw(self, screen, ui_font):
        dialogue_rect = pygame.Rect(
        0,
        MAP_HEIGHT,
        SCREEN_WIDTH,
        SCREEN_HEIGHT - MAP_HEIGHT
        )
        current_node = self.nodes[self.current_index]
        if "options" in current_node:
            question_text = ui_font.render(self.language_data[current_node["text_id"]], True, "black")
            position = (
                dialogue_rect.x + 20,
                dialogue_rect.y + 20
            )
            screen.blit(question_text, position)               
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


    def start_encounter(self, encounter_id, player):
        self.sequence = []
        self.add_encounter_to_sequence(encounter_id, player)

    def start_loot_search(self, encounter_id, player):
        self.sequence = []
        scenario = SEARCH_AREAS[encounter_id]
        self.sequence.append(scenario["text_id"])
        containers = scenario["containers"]
        for container in containers:
            node = TEXT_NODES["engage"].copy()

    def add_encounter_to_sequence(self, encounter_id, player):
        encounter = ENCOUNTERS[encounter_id]
        # detect correct initial text
        self.sequence.append(encounter["text_id"])
        enemies = encounter["enemies"]
        for enemy in enemies:
            # generate encounter text
            node = TEXT_NODES["engage"].copy()

            node["variables"] = {
                "player": player.name,
                "player_level": player.level,
                "player_class": player.game_class,
                "enemy": enemy.name,
                "enemy_level": enemy.level,
                "enemy_class": enemy.game_class
            }
            self.sequence.append(node)
            # run encounter logic and store result
            result = self.simulate_encounter(player, enemy)
            # loss
            if result == "death":
                node = TEXT_NODES["loss"].copy()
                node["variables"] = {
                    "enemy": enemy.name
                }
                self.sequence.append(node)
                break
            # win
            else:
                exp, loot, coins = result
                node = TEXT_NODES["win"].copy()
                node["variables"] = {
                    "enemy": enemy.name
                }
                self.sequence.append(node)
                # set exp text
                node = TEXT_NODES["xp"].copy()
                node["variables"] = {
                    "exp": exp
                }
                self.sequence.append(node)
                # set loot text
                node = TEXT_NODES["loot"].copy()
                loot_lines = [f"{coins} Coins"] + loot
                loot_text = "\n".join(loot_lines)
                node["variables"] = {
                    "loot": loot_text
                }
                self.sequence.append(node)

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



    def simulate_encounter(self, enemy, player):
        if combat_placeholder(player, enemy) == False:
            return "death"

        loot, coins = calc_loot(enemy)
        exp = enemy.level

        player.experience += exp
        player.inventory.extend(loot)
        player.coins += coins

        return exp, loot, coins
