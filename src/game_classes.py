



default_abilities = {
    "main": "strike",
    "ultimate": "lunge",
    "avoidance": "dodge"
}

class Default():
    def __init__(self):
        self.name = "Default"
        self.abilities = default_abilities

class Farmer():
    def __init__(self):
        self.name = "Default"
        self.abilities = default_abilities
    def __str__(self):
        return "Farmer"

beast_abilities = {
    "main": "bite",
    "ultimate": "ravage",
    "avoidance": "dodge"
}

class Beast():
    def __init__(self):
        self.name = "Beast"
        self.abilities = beast_abilities





GAME_CLASSES = {
    "Beast": Beast,
    "Farmer": Farmer,
    "Warrior": Default,
    "Rogue": Default,
    "Mage": Default,
    "Paladin": Default,
    "Reaper": Default,
    "Warlock": Default
}