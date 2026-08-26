

DIALOGUE = {
    "intro": {
        "text_id": "dialogue.intro_1",
        "next": "intro 2"
    },

    "intro 2": {
            "text_id": "dialogue.intro_2",
            "next": "intro 3"
        },

    "intro 3": {
            "text_id": "dialogue.intro_3",
            "next": "intro 4"
        },

    "intro 4": {
            "text_id": "dialogue.intro_4",
            "next": "intro 5"
        },

    "intro 5": {
            "text_id": "dialogue.intro_5",
            "next": "look around upstairs"
        },

    "intro wake": {
        "text_id": "dialogue.intro_wake",
        "next": "look around upstairs"
    },




    "look around downstairs": {
        "text_id": "dialogue.look_around_downstairs",
        "options": {
            1: {
                "text_id": "dialogue.option.open_trapdoor",
                "next": "trapdoor"
            },
            2: {
                "text_id": "dialogue.option.go_upstairs",
                "next": "stairs upward"
            },
            3: {
                "text_id": "dialogue.option.leave_door",
                "next": "door"
            },
            4: {
                "text_id": "dialogue.option.examine_table",
                "next": "table"
            }
        }
    },





    "trapdoor": {
        "text_id": "dialogue.trapdoor",
        "next": "trapdoor choice",

    },

    "trapdoor choice": {
        "text_id": "dialogue.trapdoor_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.trapdoor_go_down",
                "next": "trapdoor climb down"
            },
            2: {
                "text_id": "dialogue.option.trapdoor_step_away",
                "next": "trapdoor walk away"
            }
        }
    },

    "trapdoor walk away": {
        "text_id": "dialogue.trapdoor_walk_away",
        "next": "look around downstairs"
    },

    "trapdoor climb down": {
        "text_id": "dialogue.trapdoor_climb_down",
        "actions": [
            {   
                "type": "check_flag",
                "target": "basement_unlocked",
                "value": True,
                "if_pass": "trapdoor pass 1",
                "if_fail": "trapdoor fail 1",
            }
        ]
    },

    "trapdoor fail 1": {
        "text_id": "dialogue.trapdoor_fail_1",
        "next": "trapdoor fail 2",
        "actions": [
            {   
                "type": "map",
                "target": "pitch black"
            }
        ]
    },

    "trapdoor fail 2": {
        "text_id": "dialogue.trapdoor_fail_2",
        "next": "You died"
    },

    "trapdoor pass 1": {
        "text_id": "dialogue.trapdoor_pass_1",
        "next": "trapdoor pass 2",
        "actions": [
            {   
                "type": "map",
                "target": "pitch black"
            }
        ]
    },

    "trapdoor pass 2": {
        "text_id": "dialogue.trapdoor_pass_2",
        "next": "basement 1",
        "actions": [
            {   
                "type": "map",
                "target": "basement"
            }
        ]
    },
    


    "stairs upward": {
        "text_id": "dialogue.stairs_to_upstairs",
        "next": "upstairs",
        "actions": [
            {   
                "type": "map",
                "target": "house_upstairs"
            }
        ]
    },

    "upstairs": {
        "text_id": "dialogue.upstairs",
        "next": "look around upstairs"
    },

    "look around upstairs": {
        "text_id": "dialogue.look_around_upstairs",
        "options": {
            1: {
                "text_id": "dialogue.option.go_to_bed",
                "next": "bed"
            },
            2: {
                "text_id": "dialogue.option.go_downstairs",
                "next": "stairs downward"
            },
            3: {
                "text_id": "dialogue.option.inspect_left_bookshelf",
                "next": "left bookshelf"
            },
            4: {
                "text_id": "dialogue.option.inspect_right_bookshelf",
                "next": "right bookshelf"
                }
            }
        },



    "bed": {
            "text_id": "dialogue.sleep_1",
            "next": "sleep"
        },

    "sleep": {
                "text_id": "dialogue.sleep_2",
                "next": "intro wake"
            },



    "stairs downward": {
        "text_id": "dialogue.stairs_downward",
        "next": "look around downstairs",
        "actions": [
            {   
                "type": "map",
                "target": "house"
            }
        ]
    },




    "left bookshelf": {
        "text_id": "dialogue.left_bookshelf",
        "actions": [
            {   
                "type": "check_flag",
                "target": "left_bookshelf_empty",
                "value": False,
                "if_pass": "tome open",
                "if_fail": "left bookshelf empty",
            }
        ]
    },

    "left bookshelf empty": {
        "text_id": "dialogue.left_bookshelf_empty",
        "next": "look around upstairs"
    },

    "tome open": {
        "text_id": "dialogue.tome_open_1",
        "next": "tome read 1"
    },

    "tome read 1": {
        "text_id": "dialogue.tome_read_1",
        "next": "tome read 2"
    },

    "tome read 2": {
        "text_id": "dialogue.tome_read_2",
        "next": "tome unlock incantation"
    },

    "tome unlock incantation": {
        "text_id": "dialogue.tome_unlock_incant",
        "next": "tome close",
        "actions": [
            {   
                "type": "set_flag",
                "target": "basement_unlocked",
                "value": True
            },
            {   
                "type": "item",
                "target": "Old Tome",
                "value": 1
            }
        ]
    },

    
    "tome close": {
        "text_id": "dialogue.tome_close",
        "next": "look around upstairs"
    },



    "right bookshelf": {
        "text_id": "dialogue.right_bookshelf",
        "actions": [
            {   
                "type": "check_flag",
                "target": "right_bookshelf_empty",
                "value": False,
                "if_pass": "forbidden react",
                "if_fail": "right bookshelf empty",
            }
        ]
    },

    "right bookshelf empty": {
        "text_id": "dialogue.right_bookshelf_empty",
        "next": "look around upstairs"
    },

    "forbidden react": {
        "text_id": "dialogue.forbidden_react",
        "options": {
            1: {
                "text_id": "dialogue.option.forbidden_read",
                "next": "forbidden open"
            },
            2: {
                "text_id": "dialogue.option.forbidden_dont_read",
                "next": "forbidden in inventory"
            }
        }
    },

    "forbidden in inventory": {
        "text_id": "dialogue.forbidden_in_inventory",
        "next": "look around upstairs",
        "actions": [
            {   
                "type": "set_flag",
                "target": "right_bookshelf_empty",
                "value": True
            },
            {   
                "type": "item",
                "target": "Book of Forbidden Knowledge",
                "value": 1
            }
        ]
    },


    "forbidden open": {
        "text_id": "dialogue.forbidden_open",
        "next": "forbidden read 1"
    },

    "forbidden read 1": {
        "text_id": "dialogue.forbidden_read_1",
        "next": "forbidden read 2"
    },

    "forbidden read 2": {
        "text_id": "dialogue.forbidden_read_2",
        "next": "forbidden read 3"
    },

    "forbidden read 3": {
        "text_id": "dialogue.forbidden_read_3",
        "next": "You collapse on the floor book"
    },



    "door": {
        "text_id": "dialogue.leave_door",
        "next": "door encounter"
    },

    "door encounter": {
        "text_id": "dialogue.door_encounter",
        "actions": [
            {   
                "type": "combat",
                "target": "door_encounter",
                "on_win": "door victory",
                "on_loss": "door death"
            }
        ]
    },

    "door death 1": {
        "text_id": "dialogue.door_death_1",
        "next": "You collapse on the floor"
    },

    "door death 2": {
        "text_id": "dialogue.door_death_2",
        "next": "You collapse on the floor"
    },

    "door death 3": {
        "text_id": "dialogue.door_death_3",
        "next": "You collapse on the floor"
    },

    "door death 4": {
        "text_id": "dialogue.door_death_4",
        "next": "You collapse on the floor"
    },


    "You collapse on the floor": {
        "text_id": "dialogue.collapse_floor",
        "next": "You collapse on the floor 2"
    },

    "You collapse on the floor 2": {
        "text_id": "dialogue.collapse_floor_2",
        "next": "You died"
    },

    "You collapse on the floor book": {
        "text_id": "dialogue.collapse_floor_book",
        "next": "You died"
    },


    "You died": {
        "text_id": "dialogue.died",
        "next": "intro wake",
        "actions": [
            {   
                "type": "map",
                "target": "house_upstairs"
            }
        ]
    },



    "table": {
        "text_id": "dialogue.table",
        "next": "inspect table",
        "actions": [
            {   
                "type": "check_flag",
                "target": "downstairs_table_empty",
                "value": False,
                "if_pass": "inspect table",
                "if_fail": "table empty",
            }
        ]
    },

    "table empty": {
        "text_id": "dialogue.table_empty",
        "next": "look around downstairs"
    },

    "inspect table": {
        "text_id": "dialogue.inspect_table",
        "options": {
            1: {
                "text_id": "dialogue.option.take_knife",
                "next": "table took knife"
            },
            2: {
                "text_id": "dialogue.option.dont_take_knife",
                "next": "table didn't take knife"
            }
        }
    },



    "table took knife": {
        "text_id": "dialogue.table_took_knife",
        "next": "look around downstairs",
        "actions": [
            {   
                "type": "set_flag",
                "target": "downstairs_table_empty",
                "value": True
            },
            {   
                "type": "item",
                "target": "Knife",
                "value": 1
            }
        ]
    },


    "table didn't take knife": {
        "text_id": "dialogue.table_didnt_take_knife",
        "next": "look around downstairs"
    },

    "basement 1": {
        "text_id": "dialogue.basement_1",
        "next": "look around the basement"
    },

    "look around the basement": {
        "text_id": "dialogue.look_around_basement",
        "options": {
            1: {
                "text_id": "dialogue.not_yet_implemented",
                "next": "Not Yet Implemented"
            },
            2: {
                "text_id": "dialogue.not_yet_implemented",
                "next": "Not Yet Implemented"
            },
            3: {
                "text_id": "dialogue.not_yet_implemented",
                "next": "Not Yet Implemented"
            },
            4: {
                "text_id": "dialogue.not_yet_implemented",
                "next": "Not Yet Implemented"
                }
            }
        },

    "Not Yet Implemented": {
        "text_id": "dialogue.not_yet_implemented",
        "next": "look around the basement"
    },






}
