



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
    def __init__(self, class_id, name, abilities, power):
        self.class_id = class_id
        self.name_id = name
        self.abilities = abilities
        self.power = power


GAME_CLASSES = {
    "Beast": GameClass(
        "Beast",
        "class.beast",
        beast_abilities,
        power=5
    ),
    "Classless": GameClass(
        "Classless",
        "class.classless",
        default_abilities,
        power=0
    ),
    "Trainee": GameClass(
        "Trainee",
        "class.trainee",
        default_abilities,
        power=5
    ),
    "Warrior": GameClass(
        "Warrior",
        "class.warrior",
        default_abilities,
        power=15
    ),
    "Rogue": GameClass(
        "Rogue",
        "class.rogue",
        default_abilities,
        power=15
    ),
    "Ranger": GameClass(
        "Ranger",
        "class.ranger",
        default_abilities,
        power=15
    ),
    "Mage": GameClass(
        "Mage",
        "class.mage",
        default_abilities,
        power=15
    ),
    "Paladin": GameClass(
        "Paladin",
        "class.paladin",
        default_abilities,
        power=20
    ),
    "Warlock": GameClass(
        "Warlock",
        "class.warlock",
        default_abilities,
        power=15
    ),
    "Reaver": GameClass(
        "Reaver",
        "class.reaver",
        default_abilities,
        power=30
    ),
    "Reaper": GameClass(
        "Reaper",
        "class.reaper",
        default_abilities,
        power=45
    ),
    "ReaperBoss": GameClass(
        "Reaper",
        "class.reaper",
        default_abilities,
        power=80
    )
}