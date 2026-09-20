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
    "search_victory": {
        "text_id": "exploration.search_victory"
    }
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
    "tunnel_1_ambush": {
        "enemies": ["giant_rat"],
        "text_id": "exploration.tunnel_1_enemies"
    },
    "tunnel_2": {
        "enemies": ["cave_goblin", "cave_goblin", "cave_goblin", "cave_goblin"],
        "text_id": "exploration.tunnel_2_enemies"
    },
    "tunnel_2_ambush": {
        "enemies": ["cave_goblin"],
        "text_id": "exploration.tunnel_2_enemies"
    },
    "sewer": {
        "enemies": ["sewer_bandit", "sewer_bandit", "sewer_bandit", "sewer_bandit", "sewer_bandit"],
        "text_id": "exploration.sewer_enemies"
    },
    "sewer_ambush": {
        "enemies": ["sewer_bandit"],
        "text_id": "exploration.sewer_enemies"
    },
    "dungeon": {
        "enemies": ["dungeon_bandit", "dungeon_bandit", "dungeon_bandit", "dungeon_bandit", "dungeon_bandit", "dungeon_bandit"],
        "text_id": "exploration.dungeon_enemies"
    },
    "dungeon_ambush": {
        "enemies": ["dungeon_bandit", "dungeon_bandit"],
        "text_id": "exploration.dungeon_enemies"
    },
    "crypt_1_enemies_1": {
        "enemies": ["skeleton", "skeleton", "zombie", "zombie"],
        "text_id": "exploration.crypt_1_enemies_1"
    },
    "crypt_1_enemies_2": {
        "enemies": ["cultist_acolyte", "cultist_acolyte", "cultist_acolyte", "cultist_acolyte"],
        "text_id": "exploration.crypt_1_enemies_2"
    },
    "crypt_1_ambush": {
        "enemies": ["skeleton_fighter", "skeleton_fighter"],
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
    "crypt_2_ambush": {
        "enemies": ["skeleton_knight", "skeleton_darkmaster"],
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
    "crypt_3_ambush": {
        "enemies": ["honor_guard", "honor_guard"],
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
                "text_id": "exploration.chest_1",
                "image": "chest",
                "encounter": "tunnel_1_ambush",
                "loot": ["Leather Gloves", "Rope"],
                "coins": 5
            }
        ]
    },
    "tunnel_2": {
        "containers": [
            {
                "type": "crate",
                "text_id": "exploration.crate_1",
                "image": "crate",
                "encounter": "tunnel_2_ambush",
                "loot": ["Strange Herb"],
                "coins": 0
            },
            {
                "type": "chest",
                "text_id": "exploration.chest_1",
                "image": "chest",
                "encounter": "tunnel_2_ambush",
                "loot": ["Gambeson", "Sewer Key"],
                "coins": 5
            }
        ]
    },
    "sewer": {
        "containers": [
            {
                "type": "crates",
                "text_id": "exploration.crates_1",
                "image": "crates",
                "encounter": "sewer_ambush",
                "loot": ["Strange Herb", "Alchemy Kit"],
                "coins": 0
            },
            {
                "type": "chest",
                "text_id": "exploration.chest_1",
                "image": "chest",
                "encounter": "sewer_ambush",
                "loot": ["Longsword", "Dungeon Key"],
                "coins": 5
            }
        ]
    },
    "dungeon": {
        "containers": [
            {
                "type": "crates",
                "text_id": "exploration.crates_1",
                "image": "crates",
                "encounter": "dungeon_ambush",
                "loot": ["Strange Herb", "Rare Ingredient"],
                "coins": 0
            },
            {
                "type": "chest",
                "text_id": "exploration.chest_1",
                "image": "chest",
                "encounter": "dungeon_ambush",
                "loot": ["Chainmail Hauberk", "Crypt Key"],
                "coins": 8
            }
        ]
    },
    "crypt_1": {
        "containers": [
            {
                "type": "Old Altar",
                "text_id": "exploration.altar_1",
                "image": "altar",
                "encounter": "crypt_1_ambush",
                "loot": ["Dark Crystal", "Old Journal Page"],
                "coins": 0
            }
        ]
    },
    "crypt_2": {
        "containers": [
            {
                "type": "Tomb",
                "text_id": "exploration.chest_2",
                "image": "tomb",
                "encounter": "crypt_2_ambush",
                "loot": ["Old Amulet"],
                "coins": 0
            }
        ]
    },
    "crypt_3": {
        "containers": [
            {
                "type": "Small Chest",
                "text_id": "exploration.small_chest",
                "image": "small chest",
                "encounter": "crypt_3_ambush",
                "loot": ["Shiny Key"],
                "coins": 0
            }
        ]
    }
}



class Exploration():
    def __init__(self, language_data, assets):
        self.current = "intro"
        self.assets = assets
        for key in ["unknown_enemy", "bandit", "cave_goblin", "giant_rat", "cultist_acolyte", "skeleton_warrior", "zombie", "skeleton", "skeleton_mage", "honor_guard", "lord_graye", "reaper_boss", "chest", "crate", "crates", "tomb", "small_chest", "altar"]:
            self.assets[key] = pygame.transform.scale(
                self.assets[key],
                (SCREEN_WIDTH, MAP_HEIGHT)
            )
        self.language_data = language_data
        self.ui = pygame.transform.scale(
            self.assets["ui_image"],
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        self.current_image = "bandit"
        self.area = None
        self.text = None
        self.options = None
        self.option_page = 0
        self.nodes = []
        self.current_index = 0
        self.result = None
        self.return_node = None



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

    #not used
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
        
        node = self.sequence[self.current_index]
        if "image" in node:
            if self.current_image != node["image"]:
                self.current_image = node["image"]
                print(
                    "IMAGE CHANGED:",
                    self.current_image,
                    self.assets[self.current_image].get_size()
                )
        if self.current_image is not None:
            image = self.assets[self.current_image]
            screen.blit(image, (0, 0))
        screen.blit(self.ui, (0, 0))
        text_string = self.language_data[node["text_id"]].format(
            **node.get("variables", {})
        )
        # AI-assisted: multiline text rendering and vertical centering logic
        # I wanted to move on top multiple lines, but it was beyond my skillset + the project has already taken longer than intended
        lines = text_string.split("\n")
        line_height = ui_font.get_linesize()
        total_height = len(lines) * line_height
        y = dialogue_rect.centery - total_height // 2

        for line in lines:
            text = ui_font.render(line, True, "black")
            rect = text.get_rect(centerx=dialogue_rect.centerx, y=y)
            screen.blit(text, rect)
            y += line_height

        
        # screen.blit(text, rect)



    def start_encounter(self, encounter_id, player):
        self.result = None
        self.sequence = []
        self.current_index = 0
        self.add_encounter_to_sequence(encounter_id, player)

    def start_loot_search(self, encounter_id, player):
        self.result = None
        self.sequence = []
        self.current_index = 0
        scenario = SEARCH_AREAS[encounter_id]
        containers = scenario["containers"]
        for container in containers:
            node = container.copy()
            self.sequence.append(node)
            print("CURRENT CHEST:", self.assets["chest"].get_size())
            node_2 = TEXT_NODES["search"].copy()
            self.sequence.append(node_2)
            encounter = self.explore_encounter()
            if encounter:
                node = TEXT_NODES["search_interrupted"].copy()
                self.sequence.append(node)
                # I think I need to create custom encounters for this
                result = self.add_encounter_to_sequence(
                    container["encounter"],
                    player
                )
                if result == "death":
                    break
                node = TEXT_NODES["search_victory"].copy()
                self.sequence.append(node)
                node = TEXT_NODES["loot"].copy()
                loot = container["loot"]
                coins = container["coins"]
                player.inventory.extend(loot)
                player.coins += coins
                loot_lines = [f"{coins} Coins"] + loot
                loot_text = "\n".join(loot_lines)
                node["variables"] = {
                    "loot": loot_text
                }
                self.sequence.append(node)
            else:
                node = TEXT_NODES["search_success"].copy()
                self.sequence.append(node)
                node = TEXT_NODES["loot"].copy()
                loot = container["loot"]
                coins = container["coins"]
                player.inventory.extend(loot)
                player.coins += coins
                loot_lines = [f"{coins} Coins"] + loot
                loot_text = "\n".join(loot_lines)
                node["variables"] = {
                    "loot": loot_text
                }
                self.sequence.append(node)


    def add_encounter_to_sequence(self, encounter_id, player):
        encounter = ENCOUNTERS[encounter_id]
        # detect correct initial text
        node = {
            "text_id": encounter["text_id"],
            "image": "unknown_enemy"
        }
        self.sequence.append(node)
        enemies = encounter["enemies"]
        for enemy_id in enemies:
            # generate encounter text
            node = TEXT_NODES["engage"].copy()
            enemy_data = ENEMIES[enemy_id]
            enemy = Character()
            enemy.create(
                enemy_data["name"],
                enemy_data["level"],
                enemy_data["game_class"],
                enemy_data["inventory"],
                enemy_data["coins"],
                enemy_data["equipped"]
            )
            node["variables"] = {
                "player": player.name,
                "player_level": player.level,
                "player_class": player.game_class.__name__,
                "enemy": enemy.name,
                "enemy_level": enemy.level,
                "enemy_class": enemy.game_class.__name__
            }
            node["image"] = enemy_data["image"]
            self.sequence.append(node)
            # run encounter logic and store result
            result = self.simulate_encounter(enemy, player)
            print("COMBAT RESULT:", result)
            print("EXPLORATION RESULT:", self.result)
            # loss
            if result == "death":
                self.result = "death"
                node = TEXT_NODES["loss"].copy()
                node["variables"] = {
                    "enemy": enemy.name
                }
                self.sequence.append(node)
                if self.current_index >= len(self.sequence):
                    print("SEQUENCE COMPLETE:", self.result)
                return "death"
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
                loot_lines = [f"{coins} Coins"] + enemy.inventory.copy()

                equipped_items = [
                    item for item in enemy.equipped.values()
                    if item is not None
                ]

                if equipped_items:
                    loot_lines.append("[Equipped Items]")

                loot_text = "\n".join(loot_lines)
                node["variables"] = {
                    "loot": loot_text
                }
                self.sequence.append(node)
        if self.current_index >= len(self.sequence):
            print("SEQUENCE COMPLETE:", self.result)
        return "win"

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
        if not combat_placeholder(player, enemy):
            return "death"

        loot, coins = calc_loot(enemy)

        exp = enemy.level * 25

        player.grant_exp(exp)
        player.inventory.extend(loot)
        player.coins += coins

        return exp, loot, coins
