



default_abilities = {
    "main": "strike",
    "ultimate": "lunge",
    "avoidance": "dodge"
}

beast_abilities = {
    "main": "bite",
    "ultimate": "ravage",
    "avoidance": "dodge"
}

class GameClass():
    def __init__(self, name, abilities, power):
        self.name_id = name
        self.abilities = abilities
        self.power = power


GAME_CLASSES = {
    "Beast": GameClass(
        "class.beast",
        beast_abilities,
        power=5
    ),
    "Farmer": GameClass(
        "class.farmer",
        default_abilities,
        power=5
    ),
    "Warrior": GameClass(
        "class.warrior",
        default_abilities,
        power=15
    ),
    "Rogue": GameClass(
        "class.rogue",
        default_abilities,
        power=15
    ),
    "Mage": GameClass(
        "class.mage",
        default_abilities,
        power=15
    ),
    "Paladin": GameClass(
        "class.paladin",
        default_abilities,
        power=25
    ),
    "Reaper": GameClass(
        "class.reaper",
        default_abilities,
        power=50
    ),
    "Warlock": GameClass(
        "class.warlock",
        default_abilities,
        power=15
    )
}