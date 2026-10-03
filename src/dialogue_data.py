

DIALOGUE = {
    "intro": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "has_died",
                "value": True,
                "if_pass": "resurrect 1",
                "if_fail": "intro 1",
            }
        ]
    },

    "intro 1": {
            "text_id": "dialogue.intro_1",
            "next": "intro 2"
        },

    "intro 2": {
            "text_id": "dialogue.intro_2",
            "next": "intro 3"
        },

    "intro 3": {
            "text_id": "dialogue.intro_3",
            "next": "look around upstairs"
        },


    "resurrect 1": {
            "text_id": "dialogue.resurrect_1",
            "next": "resurrect 2"
        },

    "resurrect 2": {
            "text_id": "dialogue.resurrect_2",
            "next": "resurrect 3"
        },

    "resurrect 3": {
            "text_id": "dialogue.resurrect_3",
            "next": "resurrect 4"
        },

    "resurrect 4": {
            "text_id": "dialogue.resurrect_4",
            "next": "resurrect 5"
        },

    "resurrect 5": {
            "text_id": "dialogue.resurrect_5",
            "next": "resurrect 6"
        },

    "resurrect 6": {
            "text_id": "dialogue.resurrect_6",
            "next": "resurrect 7"
        },

    "resurrect 7": {
            "text_id": "dialogue.resurrect_7",
            "next": "resurrect 8"
        },

    "resurrect 8": {
            "text_id": "dialogue.resurrect_8",
            "next": "resurrect 9"
        },

    "resurrect 9": {
            "text_id": "dialogue.resurrect_9",
            "next": "look around upstairs"
        },

    "intro wake": {
        "text_id": "dialogue.intro_wake",
        "next": "look around upstairs"
    },

    "hardcore death reset": {
        "text_id": "dialogue.hardcore_death_reset",
        "next": "hardcore death reset 2"
    },

    "hardcore death reset 2": {
        "text_id": "dialogue.hardcore_death_reset_2",
        "next": "look around upstairs"
    },

    "look around upstairs": {
        "text_id": "dialogue.look_around_upstairs",
        "options": {
            1: {
                "text_id": "dialogue.option.inspect_bed_chest",
                "next": "bed chest"
            },
            2: {
                "text_id": "dialogue.option.go_to_bed",
                "next": "bed options"
            },
            3: {
                "text_id": "dialogue.option.go_downstairs",
                "next": "stairs downward"
            },
            4: {
                "text_id": "dialogue.more_options",
                "next": "look around upstairs 2"
                }
            }
        },

    "look around upstairs 2": {
        "text_id": "dialogue.look_around_upstairs",
        "options": {
            1: {
                "text_id": "dialogue.option.inspect_left_bookshelf",
                "next": "left bookshelf"
            },
            2: {
                "text_id": "dialogue.option.inspect_right_bookshelf",
                "next": "right bookshelf"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "look around upstairs 2"
            },
            4: {
                "text_id": "dialogue.previous_options",
                "next": "look around upstairs"
                }
            }
        },


    "bed chest": {
            "text_id": "dialogue.bed_chest_1",
            "next": "bed chest 2",
            "actions": [
                {   
                    "type": "check_flag",
                    "target": "inventory_unlocked",
                    "value": False,
                    "if_pass": "bed chest 2",
                    "if_fail": "bed chest empty",
                }
            ]
        },

    "bed chest empty": {
            "text_id": "dialogue.bed_chest_empty",
            "next": "look around upstairs"
        },

    "bed chest 2": {
            "text_id": "dialogue.bed_chest_2",
            "next": "bed chest 3"
        },

    "bed chest 3": {
            "text_id": "dialogue.bed_chest_3",
            "next": "bed chest 4"
        },

    "bed chest 4": {
            "text_id": "dialogue.bed_chest_4",
            "next": "bed chest 5",
            "actions": [
                {   
                    "type": "equip",
                    "target": "White Linen Shirt",
                    "slot": "shirt",
                    "value": 1
                },
                {   
                    "type": "equip",
                    "target": "Dark Brown Trousers",
                    "slot": "pants",
                    "value": 1
                },
                {   
                    "type": "equip",
                    "target": "Leather Belt",
                    "slot": "waist",
                    "value": 1
                },
                {   
                    "type": "equip",
                    "target": "wool stockings",
                    "slot": "feet",
                    "value": 1
                }
            ]
        },

    "bed chest 5": {
            "text_id": "dialogue.bed_chest_5",
            "next": "bed chest 6",
            "actions": [
                {   
                    "type": "equip",
                    "target": "Nicholas' Satchel",
                    "slot": "bag",
                    "value": 1
                }
            ]
        },

    "bed chest 6": {
            "text_id": "dialogue.bed_chest_6",
            "next": "look around upstairs",
            "actions": [
                {
                   "type": "set_flag",
                    "target": "inventory_unlocked",
                    "value": True 
                }
            ]
        },


    "bed": {
            "text_id": "dialogue.sleep_1",
            "next": "sleep"
        },

    "sleep": {
                "text_id": "dialogue.sleep_2",
                "next": "intro wake"
            },

    "bed options": {
        "text_id": "dialogue.bed_options",
        "options": {
            1: {
                "text_id": "dialogue.option.save_game",
                "next": "save game"
            },
            2: {
                "text_id": "dialogue.option.rest_in_bed",
                "next": "rest bed"
            },
            3: {
                "text_id": "dialogue.option.do_nothing",
                "next": "look around upstairs"
            },
            4: {
                "text_id": "dialogue.option.main_menu",
                "next": "main menu"
            }
        }
    },

    "rest bed": {
        "text_id": "dialogue.rest_bed",
        "next": "restore bed"
    },

    "restore bed": {
        "text_id": "dialogue.restore_bed",
        "next": "intro wake",
        "actions": [
            {
                "type": "restore_health",
                "target": "full",
                "value": 100
            }
        ]
    },

    "save game": {
        "text_id": "dialogue.save_game",
        "options": {
            1: {
                "text_id": "dialogue.option.save_game_yes",
                "next": "save game yes"
            },
            2: {
                "text_id": "dialogue.option.save_game_no",
                "next": "save game no"
            },
            3: {
                "text_id": "dialogue.option.do_nothing",
                "next": "look around upstairs"
            },
            4: {
                "text_id": "dialogue.option.main_menu",
                "next": "main menu"
            }
        }
    },

    "save game yes": {
        "text_id": "dialogue.save_game_yes",
        "next": "rest bed",
        "actions": [
            {
                "type": "save_game",
                "target": "farmhouse_bed"
            }
        ]
    },

    "save game no": {
        "text_id": "dialogue.save_game_no",
        "next": "bed options"
    },

    "main menu": {
        "text_id": "dialogue.main_menu",
        "options": {
            1: {
                "text_id": "dialogue.option.main_menu_yes",
                "next": "main menu yes"
            },
            2: {
                "text_id": "dialogue.option.main_menu_no",
                "next": "main menu no"
            },
            3: {
                "text_id": "dialogue.option.do_nothing",
                "next": "look around upstairs"
            },
            4: {
                "text_id": "dialogue.option.do_nothing",
                "next": "look around upstairs"
            }
        }
    },


    "main menu yes": {
        "text_id": "dialogue.main_menu_yes",
        "actions": [
            {
                "type": "main_menu"
            }
        ]
    },

    "main menu no": {
        "text_id": "dialogue.main_menu_no",
        "next": "bed options"
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
                "target": "inventory_unlocked",
                "value": True,
                "if_pass": "left bookshelf check empty",
                "if_fail": "no inventory",
            }
        ]
    },

    "left bookshelf check empty": {
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

    "no inventory": {
        "text_id": "dialogue.no_inventory",
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
                "target": "left_bookshelf_empty",
                "value": True
            },
            {   
                "type": "item",
                "target": "Old Tome",
                "value": 1
            },
            {   
                "type": "set_flag",
                "target": "basement_unlocked",
                "value": True
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
                "target": "inventory_unlocked",
                "value": True,
                "if_pass": "right bookshelf check treatise",
                "if_fail": "no inventory",
            }
        ]
    },


    "right bookshelf check treatise": {
        "text_id": "dialogue.right_bookshelf",
        "actions": [
            {   
                "type": "check_flag",
                "target": "combat_treatise_taken",
                "value": False,
                "if_pass": "treatise choice",
                "if_fail": "right bookshelf check forbidden",
            }
        ]
    },

    "right bookshelf check forbidden": {
        "text_id": "dialogue.right_bookshelf",
        "actions": [
            {   
                "type": "check_flag",
                "target": "forbidden_book_taken",
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


    "treatise choice": {
        "text_id": "dialogue.treatise_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.treatise_read",
                "next": "treatise read"
            },
            2: {
                "text_id": "dialogue.option.treatise_leave",
                "next": "treatise leave"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "treatise choice"
            },
            4: {
                "text_id": "dialogue.option.empty",
                "next": "treatise choice"
            },
        }
    },

    "treatise leave": {
        "text_id": "dialogue.treatise_leave",
        "next": "look around upstairs"
    },


    "treatise read": {
        "text_id": "dialogue.treatise_read",
        "next": "treatise read 2"
    },

    "treatise read 2": {
        "text_id": "dialogue.treatise_read_2",
        "next": "forbidden covered",
        "actions": [
            {   
                "type": "set_flag",
                "target": "combat_treatise_taken",
                "value": True
            },
            {   
                "type": "item",
                "target": "Combat Treatise",
                "value": 1
            }
        ]
    },

    "forbidden covered": {
        "text_id": "dialogue.forbidden covered",
        "next": "forbidden covered 2"
    },

    "forbidden covered 2": {
        "text_id": "dialogue.forbidden covered 2",
        "next": "forbidden react"
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
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "forbidden react"
            },
            4: {
                "text_id": "dialogue.option.empty",
                "next": "forbidden react"
            },
        }
    },

    "forbidden in inventory": {
        "text_id": "dialogue.forbidden_in_inventory",
        "next": "look around upstairs",
        "actions": [
            {   
                "type": "set_flag",
                "target": "forbidden_book_taken",
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



    "look around downstairs": {
        "text_id": "dialogue.look_around_downstairs",
        "options": {
            1: {
                "text_id": "dialogue.option.leave_door",
                "next": "door check"
                
            },
            2: {
                "text_id": "dialogue.option.boots_by_door",
                "next": "check by door"
            },
            3: {
                "text_id": "dialogue.option.check_window",
                "next": "check window"
            },
            4: {
                "text_id": "dialogue.more_options",
                "next": "look around downstairs 2"
            }
        }
    },

    "look around downstairs 2": {
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
                "text_id": "dialogue.option.examine_table",
                "next": "table"
            },
            4: {
                "text_id": "dialogue.more_options",
                "next": "look around downstairs 3"
            }
        }
    },

    "look around downstairs 3": {
        "text_id": "dialogue.look_around_downstairs",
        "options": {
            1: {
                "text_id": "dialogue.option.inspect_downstairs_chest",
                "next": "inspect downstairs chest"
            },
            2: {
                "text_id": "dialogue.option.empty",
                "next": "look around downstairs 3"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "look around downstairs 3"
            },
            4: {
                "text_id": "dialogue.previous_options",
                "next": "look around downstairs"
            }
        }
    },


    "check by door": {
        "text_id": "dialogue.check_by_door",
        "next": "boots by door",
        "actions": [
            {   
                "type": "check_flag",
                "target": "downstairs_boots_taken",
                "value": False,
                "if_pass": "boots by door",
                "if_fail": "boots taken",
            }
        ]

    },

    "boots taken": {
        "text_id": "dialogue.boots_taken",
        "next": "look around downstairs",

    },


    "boots by door": {
        "text_id": "dialogue.boots_by_door",
        "next": "take boots",

    },

    "take boots": {
        "text_id": "dialogue.take_boots",
        "next": "look around downstairs",
        "actions": [
            {   
                "type": "set_flag",
                "target": "downstairs_boots_taken",
                "value": True
            },
            {   
                "type": "equip",
                "target": "Sturdy brown boots",
                "slot": "shoes",
                "value": 1
            }
        ]
    },

    "inspect downstairs chest": {
        "text_id": "dialogue.inspect_downstairs_chest",
        "actions": [
            {   
                "type": "check_flag",
                "target": "downstairs_chest_empty",
                "value": False,
                "if_pass": "open downstairs chest",
                "if_fail": "downstairs chest empty",
            }
        ]
    },

    "open downstairs chest": {
        "text_id": "dialogue.open_downstairs_chest",
        "next": "take hunting sword",
    },

    "downstairs chest choice": {
        "text_id": "dialogue.downstairs_chest_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.take_hunt_sword",
                "next": "take hunting sword"
            },
            2: {
                "text_id": "dialogue.option.leave_hunt_sword",
                "next": "leave hunting sword"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "downstairs chest choice"
            },
            4: {
                "text_id": "dialogue.option.empty",
                "next": "downstairs chest choice"
            },
        }
    },

    "leave hunting sword": {
        "text_id": "dialogue.leave_hunt_sword",
        "next": "look around downstairs",

    },


    "take hunting sword": {
        "text_id": "dialogue.take_hunt_sword",
        "next": "take hunting sword 2",
        "actions": [
            {   
                "type": "set_flag",
                "target": "downstairs_chest_empty",
                "value": True
            },
            {   
                "type": "equip",
                "target": "Hunting Sword",
                "value": 1
            }
        ]
    },

    "take hunting sword 2": {
        "text_id": "dialogue.take_hunt_sword_2",
        "next": "look around downstairs",

    },

    "downstairs chest empty": {
        "text_id": "dialogue.downstairs_chest_empty",
        "next": "look around downstairs",

    },

    "check window": {
        "text_id": "dialogue.check_window",
        "next": "window react",

    },

    "window react": {
        "text_id": "dialogue.window_react",
        "next": "look around downstairs",

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
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "trapdoor choice"
            },
            4: {
                "text_id": "dialogue.option.empty",
                "next": "trapdoor choice"
            },
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
                "target": "inventory_unlocked",
                "value": True,
                "if_pass": "trapdoor climb down 2",
                "if_fail": "trapdoor need bag",
            }
        ]
    },

    "trapdoor climb down 2": {
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

    "trapdoor need bag": {
        "text_id": "dialogue.no_inventory",
        "next": "look around downstairs",
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
        "next": "You died",
        "actions": [
            {   
                "type": "show_scene",
                "target": "trapdoor death"
            }
        ]
    },

    "trapdoor pass 1": {
        "text_id": "dialogue.trapdoor_pass_1",
        "actions": [
            {   
                "type": "map",
                "target": "pitch black"
            },
            {   
                "type": "check_flag",
                "target": "basement_walls_broken",
                "value": True,
                "if_pass": "trapdoor pass b2",
                "if_fail": "trapdoor pass 2",
            }
        ]
    },


    "trapdoor pass b2": {
        "text_id": "dialogue.trapdoor_climb_down",
        "next": "basement 2",
        "actions": [
            {   
                "type": "map",
                "target": "basement 2"
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


    "door check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "door_boss_defeated",
                "value": True,
                "if_pass": "outro choice",
                "if_fail": "door check 2",
            }
        ]
    },

    "door check 2": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "front_door_encountered",
                "value": True,
                "if_pass": "door",
                "if_fail": "door check 3",
            }
        ]
    },



    "door check 3": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "church_info_obtained",
                "value": True,
                "if_pass": "prepare to leave b",
                "if_fail": "prepare to leave",
            }
        ]
    },

    "prepare to leave": {
        "text_id": "dialogue.door_1",
        "next": "prepare to leave 2"
    },

    "prepare to leave 2": {
        "text_id": "dialogue.door_2",
        "next": "go outside",        
        "actions": [
            {
                "type": "set_flag",
                "target": "front_door_encountered",
                "value": True
            }
        ]
    },

    "prepare to leave b": {
        "text_id": "dialogue.door_b1",
        "next": "prepare to leave b2"
    },

    "prepare to leave b2": {
        "text_id": "dialogue.door_b2",
        "next": "go outside",        
        "actions": [
            {
                "type": "set_flag",
                "target": "front_door_encountered",
                "value": True
            }
        ]
    },


    "door": {
        "text_id": "dialogue.leave_door",
        "next": "go outside",        
        "actions": [
            {
                "type": "set_flag",
                "target": "front_door_encountered",
                "value": True
            }
        ]
    },

    "go outside": {
        "text_id": "dialogue.go_outside",
        "next": "door encounter",
        "actions": [
            {   
                "type": "map",
                "target": "farm outside"
            },
        ]
    },


    "door encounter": {
        "text_id": "dialogue.door_encounter",
        "next": "door encounter boss",
        "actions": [
            {   
                "type": "encounter",
                "target": "door_encounter"
            }
        ]
    },

    "door encounter boss": {
        "text_id": "dialogue.door_boss",
        "next": "door encounter boss 2"
    },


    "door encounter boss 2": {
        "text_id": "dialogue.door_boss_2",
        "next": "door encounter boss 3"
    },

    "door encounter boss 3": {
        "text_id": "dialogue.door_boss_3",
        "next": "door encounter boss 4"
    },

    "door encounter boss 4": {
        "text_id": "dialogue.door_boss_4",
        "next": "door encounter boss 5"
    },

    "door encounter boss 5": {
        "text_id": "dialogue.door_boss_5",
        "next": "door encounter boss 6"
    },

    "door encounter boss 6": {
        "text_id": "dialogue.door_boss_6",
        "next": "farm saved 1",
        "actions": [
            {   
                "type": "encounter",
                "target": "door_encounter_boss"
            }
        ]
    },

    "door death 1": {
        "text_id": "dialogue.door_death_1",
        "next": "You collapse on the floor",
        "actions": [
            {   
                "type": "show_scene",
                "target": "door death spear"
            }
        ]
    },

    "door death 2": {
        "text_id": "dialogue.door_death_2",
        "next": "You collapse on the floor",
        "actions": [
            {   
                "type": "show_scene",
                "target": "door death arrow"
            }
        ]
    },

    "door death 3": {
        "text_id": "dialogue.door_death_3",
        "next": "You collapse on the floor",
        "actions": [
            {   
                "type": "show_scene",
                "target": "door death leg"
            }
        ]
    },

    "door death 4": {
        "text_id": "dialogue.door_death_4",
        "next": "You collapse on the floor",
        "actions": [
            {   
                "type": "show_scene",
                "target": "door death mind"
            }
        ]
    },


    # ending path
    # rush to shed
    "farm saved 1": {
        "text_id": "dialogue.farm_saved_1",
        "next": "farm saved 2",        
        "actions": [
            {
                "type": "set_flag",
                "target": "door_boss_defeated",
                "value": True
            }
        ]
    },

    # call out to family
    "farm saved 2": {
        "text_id": "dialogue.farm_saved_2",
        "next": "farm saved 3"
    },

    # hear them open
    "farm saved 3": {
        "text_id": "dialogue.farm_saved_3",
        "next": "farm saved 4"
    },

    # reunited
    "farm saved 4": {
        "text_id": "dialogue.farm_saved_4",
        "next": "good ending 1"
    },


    # happy ending
    "good ending 1": {
        "text_id": "dialogue.good_ending_1",
        "next": "save game 2",
        "actions": [
            {   
                "type": "show_scene",
                "target": "good ending 1"
            }
        ]
    },

    # save choice
    "save game 2": {
        "text_id": "dialogue.save_game_2",
        "options": {
            1: {
                "text_id": "dialogue.option.save_game_yes_2",
                "next": "save game yes"
            },
            2: {
                "text_id": "dialogue.option.save_game_no_2",
                "next": "return to house"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "save game 2"
            },
            4: {
                "text_id": "dialogue.option.main_menu",
                "next": "main menu"
            }
        }
    },

    "return to house": {
        "text_id": "dialogue.return_to_house",
        "next": "look around downstairs",
        "actions": [
            {   
                "type": "map",
                "target": "house"
            }
        ]
    },


    "You collapse on the floor": {
        "text_id": "dialogue.collapse_floor",
        "next": "You collapse on the floor 2",
        "actions": [
            {   
                "type": "show_scene",
                "target": "door death collapse"
            }
        ]
    },

    "You collapse on the floor 2": {
        "text_id": "dialogue.collapse_floor_2",
        "next": "You collapse on the floor 3"
    },

    "You collapse on the floor 3": {
        "text_id": "dialogue.collapse_floor_3",
        "next": "You died",
        "actions": [
            {   
                "type": "show_map",
                "target": "pitch black"
            }
        ]
    },

    "You collapse on the floor book": {
        "text_id": "dialogue.collapse_floor_book",
        "next": "You died",
        "actions": [
            {   
                "type": "show_scene",
                "target": "collapse book"
            }
        ]
    },


    "You died": {
        "text_id": "dialogue.died",
        "next": "reload after death"
    },

    "reload after death": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "death"
            },
            {   
                "type": "show_map",
                "target": "pitch black"
            }      
        ]
    },

    "table": {
        "text_id": "dialogue.table",
        "actions": [
            {   
                "type": "check_flag",
                "target": "downstairs_table_empty",
                "value": False,
                "if_pass": "table check inventory",
                "if_fail": "table empty",
            }
        ]
    },

    "table check inventory": {
        "text_id": "dialogue.table",
        "actions": [
            {   
                "type": "check_flag",
                "target": "inventory_unlocked",
                "value": True,
                "if_pass": "inspect table",
                "if_fail": "no inventory",
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
                "text_id": "dialogue.option.take_bread",
                "next": "table took bread"
            },
            2: {
                "text_id": "dialogue.option.dont_take_bread",
                "next": "table didn't take bread"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "inspect table"
            },
            4: {
                "text_id": "dialogue.option.empty",
                "next": "inspect table"
            },
        }
    },



    "table took bread": {
        "text_id": "dialogue.table_took_bread",
        "next": "look around downstairs",
        "actions": [
            {   
                "type": "set_flag",
                "target": "downstairs_table_empty",
                "value": True
            },
            {   
                "type": "item",
                "target": "Bread",
                "value": 1
            }
        ]
    },


    "table didn't take bread": {
        "text_id": "dialogue.table_didnt_take_bread",
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
                "text_id": "dialogue.option.inspect_tools",
                "next": "inspect tools"
            },
            2: {
                "text_id": "dialogue.option.inspect_basement_chest",
                "next": "inspect basement chest"
            },
            3: {
                "text_id": "dialogue.option.inspect_walls",
                "next": "inspect walls"
            },
            4: {
                "text_id": "dialogue.option.return_main_floor",
                "next": "climb to main floor"
                }
            }
        },

    # notice the chest 
    "inspect basement chest": {
        "text_id": "dialogue.inspect_basement_chest",
        "next": "basement chest check"
    },    

    # check if its recognized -> "family_history_known" must be True or else it just is a locked chest
    "basement chest check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "family_history_known",
                "value": True,
                "if_pass": "paladin chest empty check",
                "if_fail": "basement chest 1",
            }
        ]
    },

    # just an old chest
    "basement chest 1": {
        "text_id": "dialogue.basement_chest_1",
        "next": "basement chest 2"
    },    

    # locked
    "basement chest 2": {
        "text_id": "dialogue.basement_chest_2",
        "next": "basement state check"
    },    


    "basement state check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "basement_walls_broken",
                "value": True,
                "if_pass": "look around the basement 2",
                "if_fail": "look around the basement",
            }
        ]
    },

    # paladin - check if looted already: True -> empty, False -> recognize chest
    "paladin chest empty check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "paladin_chest_looted",
                "value": True,
                "if_pass": "paladin chest empty",
                "if_fail": "paladin chest 1",
            }
        ]
    },

    # chest empty
    "paladin chest empty": {
        "text_id": "dialogue.paladin_chest_empty",
        "next": "basement state check" # checking just to be safe, even though impossible
    },  

    # recognize it
    "paladin chest 1": {
        "text_id": "dialogue.paladin_chest_1",
        "next": "paladin chest key check"
    },

    # checks if you got the key
    "paladin chest key check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "crypt_3_empty",
                "value": True,
                "if_pass": "paladin chest 2",
                "if_fail": "paladin chest locked",
            }
        ]
    },

    # locked, but it has to be somewhere in the crypt
    "paladin chest locked": {
        "text_id": "dialogue.paladin_chest_locked",
        "next": "basement state check" # being safe
    },

    # I have the key, so slowly open
    "paladin chest 2": {
        "text_id": "dialogue.paladin_chest_2",
        "next": "paladin chest 3"
    },

    # old armor, sword and amulet are inside
    "paladin chest 3": {
        "text_id": "dialogue.paladin_chest_3",
        "next": "paladin chest class check",
        "actions": [
            {   
                "type": "set_flag",
                "target": "paladin_chest_looted",
                "value": True
            },
            {   
                "type": "item",
                "target": "Paladin Relics",
                "value": 1
            }
        ]
    },

    # check is a reaper or not
    "paladin chest class check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_class",
                "target": "Reaper",
                "if_pass": "paladin chest reaper",
                "if_fail": "paladin chest 4",
            }
        ]
    },

    # reaper -> not interested -> leave
    "paladin chest reaper": {
        "text_id": "dialogue.paladin_chest_reaper",
        "next": "basement state check"
    },

    # you remember the tome describing the paladin initiation ritual
    "paladin chest 4": {
        "text_id": "dialogue.paladin_chest_4",
        "next": "paladin chest 5"
    },

    # you need to go to an altar. You remember the one below the church back in the crypt.
    "paladin chest 5": {
        "text_id": "dialogue.paladin_chest_5",
        "next": "basement state check"
    },



    "inspect tools": {
        "text_id": "dialogue.inspect_tools",
        "actions": [
            {   
                "type": "check_flag",
                "target": "basement_tools_taken",
                "value": False,
                "if_pass": "tools choice",
                "if_fail": "tools taken",
            }
        ]
    },

    "tools taken": {
        "text_id": "dialogue.tools_taken",
        "next": "look around the basement"
    },

    "tools choice": {
        "text_id": "dialogue.tools_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.take_hammer_chisel",
                "next": "take tools"
            },
            2: {
                "text_id": "dialogue.option.take_nothing",
                "next": "take nothing"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "tools choice"
            },
            4: {
                "text_id": "dialogue.option.empty",
                "next": "tools choice"
            }
        }
    },

    "take tools": {
        "text_id": "dialogue.take_tools",
        "next": "look around the basement",
        "actions": [
            {   
                "type": "set_flag",
                "target": "basement_tools_taken",
                "value": True
            },
            {   
                "type": "item",
                "target": "Hammer",
                "value": 1
            },
            {   
                "type": "item",
                "target": "Chisel",
                "value": 1
            }
        ]
    },

    "take nothing": {
        "text_id": "dialogue.take_nothing",
        "next": "look around the basement"
    },



    "inspect walls": {
        "text_id": "dialogue.inspect_walls",
        "next": "walls choice"
    },

    "walls choice": {
        "text_id": "dialogue.walls_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.inspect_left_wall",
                "next": "inspect left wall"
            },
            2: {
                "text_id": "dialogue.option.inspect_right_wall",
                "next": "inspect right wall"
            },
            3: {
                "text_id": "dialogue.option.inspect_top_wall",
                "next": "inspect top wall"
            },
            4: {
                "text_id": "dialogue.option.inspect_bottom_wall",
                "next": "inspect bottom wall"
            }
        }
    },

    "inspect left wall": {
        "text_id": "dialogue.inspect_left_wall",
        "actions": [
            {   
                "type": "check_flag",
                "target": "basement_left_wall_checked",
                "value": False,
                "if_pass": "wall normal",
                "if_fail": "done wall",
            }
        ]
    },

    "inspect right wall": {
        "text_id": "dialogue.inspect_right_wall",
        "next": "right wall loose bricks"
    },

    "inspect top wall": {
        "text_id": "dialogue.inspect_top_wall",
        "actions": [
            {   
                "type": "check_flag",
                "target": "basement_top_wall_checked",
                "value": False,
                "if_pass": "wall normal",
                "if_fail": "done wall",
            }
        ]
    },

    "inspect bottom wall": {
        "text_id": "dialogue.inspect_bottom_wall",
        "next": "bottom wall loose bricks"
    },

    "done wall": {
        "text_id": "dialogue.checked_wall",
        "next": "walls choice"
    },

    "wall normal": {
        "text_id": "dialogue.wall_normal",
        "next": "walls choice"
    },

    "right wall loose bricks": {
        "text_id": "dialogue.right_wall_loose",
        "actions": [
            {   
                "type": "check_flag",
                "target": "basement_tools_taken",
                "value": True,
                "if_pass": "wall use tools",
                "if_fail": "wall need tools",
            }
        ]
    },

    "bottom wall loose bricks": {
        "text_id": "dialogue.bottom_wall_loose",
        "actions": [
            {   
                "type": "check_flag",
                "target": "basement_tools_taken",
                "value": True,
                "if_pass": "wall use tools",
                "if_fail": "wall need tools",
            }
        ]
    },

    "wall need tools": {
        "text_id": "dialogue.wall_need_tools",
        "next": "look around the basement"
    },

    "wall use tools": {
        "text_id": "dialogue.wall_use_tools",
        "next": "basement key found"
    },


    "basement key found": {
        "text_id": "dialogue.basement_key_found",
        "next": "basement door revealed",
        "actions": [
            {   
                "type": "set_flag",
                "target": "basement_key_found",
                "value": True
            },
            {   
                "type": "item",
                "target": "Basement Key",
                "value": 1
            }
        ]
    },


    "basement door revealed": {
        "text_id": "dialogue.basement_door_revealed",
        "next": "basement door choice",
        "actions": [
            {
                "type": "set_flag",
                "target": "basement_walls_broken",
                "value": True
            },
            {   
                "type": "map",
                "target": "basement 2"
            }
        ]
    },

    "basement door choice": {
        "text_id": "dialogue.basement_door_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.listen_door",
                "next": "listen to door"
            },
            2: {
                "text_id": "dialogue.option.open_door",
                "next": "basement door key check"
            },
            3: {
                "text_id": "dialogue.option.step_away",
                "next": "look around the basement 2"
            },
            4: {
                "text_id": "dialogue.option.empty",
                "next": "basement door choice"
            }
        }
    },

    "listen to door": {
        "text_id": "dialogue.listen_door",
        "next": "listen door 2"
    },

    "listen door 2": {
        "text_id": "dialogue.listen_door_2",
        "next": "basement door choice"
    },


    "basement door key check": {
        "text_id": "dialogue.basement_door_inspect",
        "actions": [
            {   
                "type": "check_flag",
                "target": "basement_key_found",
                "value": True,
                "if_pass": "basement door lock check",
                "if_fail": "basement door inspect",
            }
        ]
    },

    "basement door lock check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "basement_door_unlocked",
                "value": True,
                "if_pass": "enter tunnel 1",
                "if_fail": "basement door unlock",
            }
        ]
    },

    "basement door inspect": {
        "text_id": "dialogue.basement_door_inspect",
        "next": "basement door locked"
    },

    "basement door locked": {
        "text_id": "dialogue.basement_door_locked",
        "next": "look around the basement 2"
    },

    "basement door unlock": {
        "text_id": "dialogue.basement_door_unlock",
        "next": "enter tunnel choice",
        "actions": [
            {
                "type": "set_flag",
                "target": "basement_door_unlocked",
                "value": True
            }
        ]
    },

    "climb to main floor": {
        "text_id": "dialogue.climb_to_main_floor",
        "next": "look around downstairs",
        "actions": [
            {   
                "type": "map",
                "target": "house"
            }
        ]
    },



    "basement 2": {
        "text_id": "dialogue.basement_2",
        "next": "look around the basement 2"
    },


    "look around the basement 2": {
        "text_id": "dialogue.look_around_basement",
        "options": {
            1: {
                "text_id": "dialogue.option.inspect_basement_door",
                "next": "basement door choice"
            },
            2: {
                "text_id": "dialogue.option.inspect_basement_chest",
                "next": "inspect basement chest"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "look around the basement 2"
            },
            4: {
                "text_id": "dialogue.option.return_main_floor",
                "next": "climb to main floor"
                }
            }
        },



    "enter tunnel choice": {
        "text_id": "dialogue.enter_tunnel_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.tunnel_enter",
                "next": "enter tunnel 1"
            },
            2: {
                "text_id": "dialogue.option.empty",
                "next": "enter tunnel check"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "enter tunnel check"
            },
            4: {
                "text_id": "dialogue.option.step_away",
                "next": "look around the basement 2"
            }
        }
    },



    "enter tunnel 1": {
        "text_id": "dialogue.enter_tunnel_1",
        "next": "tunnel 1 intro",
        "actions": [
            {   
                "type": "map",
                "target": "tunnel 1"
            }
        ]
    },

    "tunnel 1 intro": {
        "text_id": "dialogue.tunnel_1_intro",
        "next": "tunnel 1 intro check"
    },

    "tunnel 1 intro check": {
        "text_id": "dialogue.tunnel_1_intro",
        "actions": [
            {   
                "type": "check_flag",
                "target": "tunnel_1_invader_slain",
                "value": True,
                "if_pass": "tunnel 1 cont B",
                "if_fail": "tunnel 1 cont",
            }
        ]
    },

    "tunnel 1 cont B": {
        "text_id": "dialogue.tunnel_1_cont_b",
        "next": "tunnel 1 choice"
    },

    "tunnel 1 cont": {
        "text_id": "dialogue.tunnel_1_cont",
        "next": "tunnel 1 encounter 1"
    },


    "tunnel 1 encounter 1": {
        "text_id": "dialogue.tunnel_1_encounter",
        "next": "tunnel 1 encounter 2"
    },

    "tunnel 1 encounter 2": {
        "text_id": "dialogue.tunnel_1_reaction_1",
        "next": "read cryptic note 1",
        "actions": [
            {   
                "type": "encounter",
                "target": "tunnel_1_encounter"
            }
        ]
    },


    "read cryptic note 1": {
        "text_id": "dialogue.cryptic_note_1",
        "next": "read cryptic note 2",
        "actions": [
            {
                "type": "set_flag",
                "target": "tunnel_1_invader_slain",
                "value": True
            },
        ]
    },

    "read cryptic note 2": {
        "text_id": "dialogue.cryptic_note_2",
        "next": "read cryptic note 3"
    },

    "read cryptic note 3": {
        "text_id": "dialogue.cryptic_note_3",
        "next": "read cryptic note 4"
    },

    "read cryptic note 4": {
        "text_id": "dialogue.cryptic_note_4",
        "next": "read cryptic note 5"
    },

    "read cryptic note 5": {
        "text_id": "dialogue.cryptic_note_5",
        "next": "read cryptic note 6"
    },

    "read cryptic note 6": {
        "text_id": "dialogue.cryptic_note_6",
        "next": "read cryptic note 7"
    },

    "read cryptic note 7": {
        "text_id": "dialogue.cryptic_note_7",
        "next": "read cryptic note 8"
    },

    "read cryptic note 8": {
        "text_id": "dialogue.cryptic_note_8",
        "next": "read cryptic note 9"
    },

    "read cryptic note 9": {
        "text_id": "dialogue.cryptic_note_9",
        "next": "read cryptic note 10"
    },

    "read cryptic note 10": {
        "text_id": "dialogue.cryptic_note_10",
        "next": "read cryptic note 11"
    },

    "read cryptic note 11": {
        "text_id": "dialogue.cryptic_note_11",
        "next": "read cryptic note 12"
    },

    "read cryptic note 12": {
        "text_id": "dialogue.cryptic_note_12",
        "next": "read cryptic note 13"
    },

    "read cryptic note 13": {
        "text_id": "dialogue.cryptic_note_13",
        "next": "read cryptic note 14"
    },

    "read cryptic note 14": {
        "text_id": "dialogue.cryptic_note_14",
        "next": "read cryptic note 15"
    },

    "read cryptic note 15": {
        "text_id": "dialogue.cryptic_note_15",
        "next": "read cryptic note 16"
    },

    "read cryptic note 16": {
        "text_id": "dialogue.cryptic_note_16",
        "next": "read cryptic note 17"
    },

    "read cryptic note 17": {
        "text_id": "dialogue.cryptic_note_17",
        "next": "read cryptic note 18"
    },

    "read cryptic note 18": {
        "text_id": "dialogue.cryptic_note_18",
        "next": "read cryptic note 19"
    },

    "read cryptic note 19": {
        "text_id": "dialogue.cryptic_note_19",
        "next": "read cryptic note 20"
    },

    "read cryptic note 20": {
        "text_id": "dialogue.cryptic_note_20",
        "next": "read cryptic note 21"
    },

    "read cryptic note 21": {
        "text_id": "dialogue.cryptic_note_21",
        "next": "read cryptic note 22"
    },

    "read cryptic note 22": {
        "text_id": "dialogue.cryptic_note_22",
        "next": "read cryptic note 23"
    },

    "read cryptic note 23": {
        "text_id": "dialogue.cryptic_note_23",
        "next": "tunnel 1 reaction 1"
    },


    "tunnel 1 reaction 1": {
        "text_id": "dialogue.tunnel_1_reaction_1",
        "next": "tunnel 1 reaction 2"
    },

    "tunnel 1 reaction 2": {
        "text_id": "dialogue.tunnel_1_reaction_2",
        "next": "tunnel 1 reaction 3"
    },


    "tunnel 1 reaction 3": {
        "text_id": "dialogue.tunnel_1_reaction_3",
        "next": "tunnel 1 choice"
    },



    "tunnel 1 choice": {
        "text_id": "dialogue.tunnel_1_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.tunnel_1_explore",
                "next": "tunnel 1 explore 1"
            },
            2: {
                "text_id": "dialogue.option.tunnel_1_enemies",
                "next": "tunnel 1 enemies 1"
            },
            3: {
                "text_id": "dialogue.option.tunnel_1_continue",
                "next": "tunnel 1 continue"
            },
            4: {
                "text_id": "dialogue.option.tunnel_1_return",
                "next": "basement return"
            }
        }
    },

    "tunnel 1 explore 1": {
        "text_id": "dialogue.tunnel_1_explore_1",
        "actions": [
            {   
                "type": "check_flag",
                "target": "tunnel_1_empty",
                "value": False,
                "if_pass": "tunnel 1 explore start",
                "if_fail": "tunnel 1 explore empty",
            }
        ]
    },

    "tunnel 1 explore start": {
        "text_id": "dialogue.tunnel_1_explore_2",
        "next": "tunnel 1 choice",
        "actions": [
            {
                "type": "set_flag",
                "target": "tunnel_1_empty",
                "value": True
            },
            {   
                "type": "explore_items",
                "target": "tunnel_1",
            }
        ]
    },

    "tunnel 1 explore empty": {
        "text_id": "dialogue.tunnel_1_explore_empty",
        "next": "tunnel 1 choice",
    },


    "tunnel 1 enemies 1": {
        "text_id": "dialogue.tunnel_1_enemies_1",
        "next": "tunnel 1 enemies 2",
        "actions": [
            {   
                "type": "encounter",
                "target": "tunnel_1",
            }
        ]
    },


    "tunnel 1 enemies 2": {
        "text_id": "dialogue.tunnel_1_enemies_2",
        "next": "tunnel 1 choice",
    },


    "basement return": {
        "text_id": "dialogue.return_to_basement",
        "next": "look around the basement 2",
        "actions": [
            {   
                "type": "map",
                "target": "basement 2"
            }
        ]
    },

    "tunnel 1 continue": {
        "text_id": "dialogue.tunnel_1_continue",
        "next": "tunnel 1 continue choice",
    },


    "tunnel 1 continue choice": {
        "text_id": "dialogue.tunnel_1_continue_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.tunnel_1_continue_2",
                "next": "tunnel 1 continue check"
            },
            2: {
                "text_id": "dialogue.option.empty",
                "next": "tunnel 1 continue choice"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "tunnel 1 continue choice"
            },
            4: {
                "text_id": "dialogue.option.tunnel_1_step_away",
                "next": "tunnel 1 choice"
            }
        }
    },


    "tunnel 1 continue check": {
        "text_id": "dialogue.tunnel_1_continue_check",
        "actions": [
            {   
                "type": "check_flag",
                "target": "tunnel_rope_placed",
                "value": True,
                "if_pass": "enter tunnel 2",
                "if_fail": "tunnel 1 rope looted check",
            }
        ]
    },

    "tunnel 1 rope looted check": {
        "text_id": "dialogue.tunnel_1_continue_check",
        "actions": [
            {   
                "type": "check_flag",
                "target": "tunnel_1_empty",
                "value": True,
                "if_pass": "tunnel 1 place rope",
                "if_fail": "tunnel 1 rope missing 1",
            }
        ]
    },


    "tunnel 1 rope missing 1": {
        "text_id": "dialogue.tunnel_1_rope_missing",
        "next": "tunnel 1 rope missing 2"
    },

    "tunnel 1 rope missing 2": {
        "text_id": "dialogue.tunnel_1_rope_missing_2",
        "next": "tunnel 1 choice"
    },

    "tunnel 1 place rope": {
        "text_id": "dialogue.tunnel_1_place_rope",
        "next": "enter tunnel 2",
        "actions": [
            {   
                "type": "set_flag",
                "target": "tunnel_rope_placed",
                "value": True
            }
        ]
    },




    "enter tunnel 2": {
        "text_id": "dialogue.enter_tunnel_2",
        "next": "tunnel 2 main check",
        "actions": [
            {   
                "type": "map",
                "target": "tunnel 2"
            }
        ]
    },

    "tunnel 2 main check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "sewer_door_unlocked",
                "value": True,
                "if_pass": "tunnel 2 intro B",
                "if_fail": "tunnel 2 intro",
            }
        ]
    },

    "tunnel 2 intro B": {
        "text_id": "dialogue.tunnel_2_intro_b",
        "next": "tunnel 2 choice"
    },

    "tunnel 2 intro": {
        "text_id": "dialogue.tunnel_2_intro",
        "next": "tunnel 2 cont"
    },

    "tunnel 2 cont": {
        "text_id": "dialogue.tunnel_2_cont",
        "next": "tunnel 2 choice"
    },


    "tunnel 2 choice": {
        "text_id": "dialogue.tunnel_2_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.tunnel_2_explore",
                "next": "tunnel 2 explore 1"
            },
            2: {
                "text_id": "dialogue.option.tunnel_2_enemies",
                "next": "tunnel 2 enemies 1"
            },
            3: {
                "text_id": "dialogue.option.tunnel_2_continue",
                "next": "tunnel 2 continue"
            },
            4: {
                "text_id": "dialogue.option.tunnel_2_return",
                "next": "tunnel 1 return"
            }
        }
    },

    "tunnel 2 explore 1": {
        "text_id": "dialogue.tunnel_2_explore_1",
        "actions": [
            {   
                "type": "check_flag",
                "target": "tunnel_2_empty",
                "value": False,
                "if_pass": "tunnel 2 explore start",
                "if_fail": "tunnel 2 explore empty",
            }
        ]
    },

    "tunnel 2 explore start": {
        "text_id": "dialogue.tunnel_2_explore_2",
        "next": "tunnel 2 choice",
        "actions": [
            {
                "type": "set_flag",
                "target": "tunnel_2_empty",
                "value": True
            },
            {   
                "type": "explore_items",
                "target": "tunnel_2",
            }
        ]
    },

    "tunnel 2 explore empty": {
        "text_id": "dialogue.tunnel_2_explore_empty",
        "next": "tunnel 2 choice",
    },


    "tunnel 2 enemies 1": {
        "text_id": "dialogue.tunnel_2_enemies_1",
        "next": "tunnel 2 enemies 2",
        "actions": [
            {   
                "type": "encounter",
                "target": "tunnel_2",
            }
        ]
    },


    "tunnel 2 enemies 2": {
        "text_id": "dialogue.tunnel_2_enemies_2",
        "next": "tunnel 2 choice",
    },


    "tunnel 1 return": {
        "text_id": "dialogue.return_to_tunnel_1",
        "next": "tunnel 1 choice",
        "actions": [
            {   
                "type": "map",
                "target": "tunnel 1"
            }
        ]
    },

    "tunnel 2 continue": {
        "text_id": "dialogue.tunnel_2_continue",
        "next": "tunnel 2 continue choice",
    },


    "tunnel 2 continue choice": {
        "text_id": "dialogue.tunnel_2_continue_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.tunnel_2_continue_2",
                "next": "tunnel 2 continue check"
            },
            2: {
                "text_id": "dialogue.option.empty",
                "next": "tunnel 2 continue choice"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "tunnel 2 continue choice"
            },
            4: {
                "text_id": "dialogue.option.tunnel_2_step_away",
                "next": "tunnel 2 choice"
            }
        }
    },


    "tunnel 2 continue check": {
        "text_id": "dialogue.tunnel_2_continue_check",
        "actions": [
            {   
                "type": "check_flag",
                "target": "sewer_door_unlocked",
                "value": True,
                "if_pass": "enter sewer",
                "if_fail": "tunnel 2 sewer key check",
            }
        ]
    },

    "tunnel 2 sewer key check": {
        "text_id": "dialogue.tunnel_2_continue_check",
        "actions": [
            {   
                "type": "check_flag",
                "target": "tunnel_2_empty",
                "value": True,
                "if_pass": "tunnel 2 unlock sewer",
                "if_fail": "tunnel 2 sewer locked 1",
            }
        ]
    },

    "tunnel 2 sewer locked 1": {
        "text_id": "dialogue.tunnel_2_sewer_locked_1",
        "next": "tunnel 2 sewer locked 2"
    },

    "tunnel 2 sewer locked 2": {
        "text_id": "dialogue.tunnel_2_sewer_locked_2",
        "next": "tunnel 2 choice"
    },

    "tunnel 2 unlock sewer": {
        "text_id": "dialogue.tunnel_2_unlock_sewer",
        "next": "enter sewer",
        "actions": [
            {   
                "type": "set_flag",
                "target": "sewer_door_unlocked",
                "value": True
            }
        ]
    },




    "enter sewer": {
        "text_id": "dialogue.enter_sewer",
        "next": "sewer main check",
        "actions": [
            {   
                "type": "map",
                "target": "sewer"
            }
        ]
    },


    "sewer main check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "dungeon_door_unlocked",
                "value": True,
                "if_pass": "sewer intro B",
                "if_fail": "sewer intro",
            }
        ]
    },

    "sewer intro B": {
        "text_id": "dialogue.sewer_intro_b",
        "next": "sewer choice"
    },


    "sewer intro": {
        "text_id": "dialogue.sewer_intro",
        "next": "sewer cont"
    },

    "sewer cont": {
        "text_id": "dialogue.sewer_cont",
        "next": "sewer choice"
    },


    "sewer choice": {
        "text_id": "dialogue.sewer_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.sewer_explore",
                "next": "sewer explore 1"
            },
            2: {
                "text_id": "dialogue.option.sewer_enemies",
                "next": "sewer enemies 1"
            },
            3: {
                "text_id": "dialogue.option.sewer_continue",
                "next": "sewer continue"
            },
            4: {
                "text_id": "dialogue.option.sewer_return",
                "next": "tunnel 2 return"
            }
        }
    },

    "sewer explore 1": {
        "text_id": "dialogue.sewer_explore_1",
        "actions": [
            {   
                "type": "check_flag",
                "target": "sewer_empty",
                "value": False,
                "if_pass": "sewer explore start",
                "if_fail": "sewer explore empty",
            }
        ]
    },

    "sewer explore start": {
        "text_id": "dialogue.sewer_explore_2",
        "next": "sewer choice",
        "actions": [
            {
                "type": "set_flag",
                "target": "sewer_empty",
                "value": True
            },
            {   
                "type": "explore_items",
                "target": "sewer",
            }
        ]
    },

    "sewer explore empty": {
        "text_id": "dialogue.sewer_explore_empty",
        "next": "sewer choice",
    },


    "sewer enemies 1": {
        "text_id": "dialogue.sewer_enemies_1",
        "next": "sewer enemies 2",
        "actions": [
            {   
                "type": "encounter",
                "target": "sewer",
            }
        ]
    },


    "sewer enemies 2": {
        "text_id": "dialogue.sewer_enemies_2",
        "next": "sewer choice",
    },


    "tunnel 2 return": {
        "text_id": "dialogue.return_to_tunnel_2",
        "next": "tunnel 2 choice",
        "actions": [
            {   
                "type": "map",
                "target": "tunnel 2"
            }
        ]
    },

    "sewer continue": {
        "text_id": "dialogue.sewer_continue",
        "next": "sewer continue choice",
    },


    "sewer continue choice": {
        "text_id": "dialogue.sewer_continue_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.sewer_continue_2",
                "next": "sewer continue check"
            },
            2: {
                "text_id": "dialogue.option.empty",
                "next": "sewer continue choice"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "sewer continue choice"
            },
            4: {
                "text_id": "dialogue.option.sewer_step_away",
                "next": "sewer choice"
            }
        }
    },


    "sewer continue check": {
        "text_id": "dialogue.sewer_continue_check",
        "actions": [
            {   
                "type": "check_flag",
                "target": "dungeon_door_unlocked",
                "value": True,
                "if_pass": "enter dungeon",
                "if_fail": "sewer dungeon key check",
            }
        ]
    },

    "sewer dungeon key check": {
        "text_id": "dialogue.sewer_continue_check",
        "actions": [
            {   
                "type": "check_flag",
                "target": "sewer_empty",
                "value": True,
                "if_pass": "sewer unlock dungeon",
                "if_fail": "sewer dungeon locked 1",
            }
        ]
    },

    "sewer dungeon locked 1": {
        "text_id": "dialogue.sewer_dungeon_locked_1",
        "next": "sewer dungeon locked 2"
    },

    "sewer dungeon locked 2": {
        "text_id": "dialogue.sewer_dungeon_locked_2",
        "next": "sewer choice"
    },

    "sewer unlock dungeon": {
        "text_id": "dialogue.sewer_unlock_dungeon",
        "next": "enter dungeon",
        "actions": [
            {   
                "type": "set_flag",
                "target": "dungeon_door_unlocked",
                "value": True
            }
        ]
    },


    "enter dungeon": {
        "text_id": "dialogue.enter_dungeon",
        "next": "dungeon main check",
        "actions": [
            {   
                "type": "map",
                "target": "dungeon"
            }
        ]
    },

    "dungeon main check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "town_door_unlocked",
                "value": True,
                "if_pass": "dungeon intro B",
                "if_fail": "dungeon intro",
            }
        ]
    },

    "dungeon intro B": {
        "text_id": "dialogue.dungeon_intro_b",
        "next": "dungeon choice"
    },

    "dungeon intro": {
        "text_id": "dialogue.dungeon_intro",
        "next": "dungeon cont"
    },

    "dungeon cont": {
        "text_id": "dialogue.dungeon_cont",
        "next": "dungeon choice"
    },


    "dungeon choice": {
        "text_id": "dialogue.dungeon_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.dungeon_explore",
                "next": "dungeon explore 1"
            },
            2: {
                "text_id": "dialogue.option.dungeon_enemies",
                "next": "dungeon enemies 1"
            },
            3: {
                "text_id": "dialogue.option.dungeon_continue",
                "next": "dungeon continue"
            },
            4: {
                "text_id": "dialogue.option.dungeon_return",
                "next": "sewer return"
            }
        }
    },

    "dungeon explore 1": {
        "text_id": "dialogue.dungeon_explore_1",
        "actions": [
            {   
                "type": "check_flag",
                "target": "dungeon_empty",
                "value": False,
                "if_pass": "dungeon explore start",
                "if_fail": "dungeon explore empty",
            }
        ]
    },

    "dungeon explore start": {
        "text_id": "dialogue.dungeon_explore_2",
        "next": "dungeon choice",
        "actions": [
            {
                "type": "set_flag",
                "target": "dungeon_empty",
                "value": True
            },
            {   
                "type": "explore_items",
                "target": "dungeon",
            }
        ]
    },

    "dungeon explore empty": {
        "text_id": "dialogue.dungeon_explore_empty",
        "next": "dungeon choice",
    },


    "dungeon enemies 1": {
        "text_id": "dialogue.dungeon_enemies_1",
        "next": "dungeon enemies 2",
        "actions": [
            {   
                "type": "encounter",
                "target": "dungeon",
            }
        ]
    },


    "dungeon enemies 2": {
        "text_id": "dialogue.dungeon_enemies_2",
        "next": "dungeon choice",
    },


    "sewer return": {
        "text_id": "dialogue.return_to_sewer",
        "next": "sewer choice",
        "actions": [
            {   
                "type": "map",
                "target": "sewer"
            }
        ]
    },

    "dungeon continue": {
        "text_id": "dialogue.dungeon_continue",
        "next": "dungeon continue choice",
    },


    "dungeon continue choice": {
        "text_id": "dialogue.dungeon_continue_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.dungeon_continue_2",
                "next": "dungeon continue check"
            },
            2: {
                "text_id": "dialogue.option.empty",
                "next": "dungeon continue choice"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "dungeon continue choice"
            },
            4: {
                "text_id": "dialogue.option.dungeon_step_away",
                "next": "dungeon choice"
            }
        }
    },


    "dungeon continue check": {
        "text_id": "dialogue.dungeon_continue_check",
        "actions": [
            {   
                "type": "check_flag",
                "target": "town_door_unlocked",
                "value": True,
                "if_pass": "enter town",
                "if_fail": "dungeon town key check",
            }
        ]
    },

    "dungeon town key check": {
        "text_id": "dialogue.dungeon_continue_check",
        "actions": [
            {   
                "type": "check_flag",
                "target": "dungeon_empty",
                "value": True,
                "if_pass": "dungeon unlock town",
                "if_fail": "dungeon town locked 1",
            }
        ]
    },

    "dungeon town locked 1": {
        "text_id": "dialogue.dungeon_town_locked_1",
        "next": "dungeon town locked 2"
    },

    "dungeon town locked 2": {
        "text_id": "dialogue.dungeon_town_locked_2",
        "next": "dungeon choice"
    },
    # now for the town
    "dungeon unlock town": {
        "text_id": "dialogue.dungeon_unlock_town",
        "next": "enter town",
        "actions": [
            {   
                "type": "set_flag",
                "target": "town_door_unlocked",
                "value": True
            }
        ]
    },


    "exit dungeon 1": {
        "text_id": "dialogue.exit_dungeon_1",
        "next": "exit dungeon check",
        "actions": [
            {   
                "type": "map",
                "target": "town"
            }
        ]
    },

    "exit dungeon check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "town_cleared", # need new flag
                "value": True,
                "if_pass": "town choice", # consider adding an intermediate node
                "if_fail": "exit dungeon 2",
            }
        ]
    },


    "exit dungeon 2": {
        "text_id": "dialogue.exit_dungeon_2",
        "next": "exit dungeon 3"
    },

    "exit dungeon 3": {
        "text_id": "dialogue.exit_dungeon_3",
        "next": "exit dungeon encounter"
    },

    "exit dungeon encounter": {
        "text_id": "dialogue.empty",
        "next": "exit dungeon 4",
        "actions": [
            {
                "type": "encounter", 
                "target": "dungeon_exit_encounter"
            }
        ]
    },

    "exit dungeon 4": {
        "text_id": "dialogue.exit_dungeon_4",
        "next": "exit dungeon 5"
    },

    "exit dungeon 5": {
        "text_id": "dialogue.exit_dungeon_5",
        "next": "exit dungeon 6"
    },

    "exit dungeon 6": {
        "text_id": "dialogue.exit_dungeon_6",
        "next": "exit dungeon 7"
    },

    "exit dungeon 7": {
        "text_id": "dialogue.exit_dungeon_7",
        "next": "exit dungeon 8"
    },

    "exit dungeon 8": {
        "text_id": "dialogue.exit_dungeon_8",
        "next": "town choice" # change later
    },






    "town choice": {
        "text_id": "dialogue.town_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.town_vendors",
                "next": "town vendors choice"
            },
            2: {
                "text_id": "dialogue.option.town_inn",
                "next": "town inn check"
            },
            3: {
                "text_id": "dialogue.option.town_continue",
                "next": "town 3"
            },
            4: {
                "text_id": "dialogue.option.sewer_secret_return",
                "next": "town sewer 1"
            }
        }
    },

    "town vendors choice": {
        "text_id": "dialogue.town_vendors_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.merchant",
                "next": "town black market"
            },
            2: {
                "text_id": "dialogue.option.blacksmith",
                "next": "town blacksmith"
            },
            3: {
                "text_id": "dialogue.option.specialty_vendor",
                "next": "town specialty"
            },
            4: {
                "text_id": "dialogue.option.town_choice",
                "next": "town choice"
            }
        }
    },



    "town inn check": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_flag",
                "target": "room_rented",
                "value": True,
                "if_pass": "town inn bed ready",
                "if_fail": "town inn 1",
            }
        ],
    },


    "town inn bed ready": {
        "text_id": "dialogue.town_inn_bed_ready",
        "next": "inn bed options",
    },


    "town inn 1": {
        "text_id": "dialogue.town_inn_1",
        "next": "town inn 2",
    },


    "town inn 2": {
        "text_id": "dialogue.town_inn_2",
        "next": "town inn 3",
    },

    "town inn 3": {
        "text_id": "dialogue.town_inn_3",
        "next": "town inn choice",
    },

    "town inn choice": {
        "text_id": "dialogue.town_inn_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.town_inn_yes",
                "next": "town inn payment",
            },
            2: {
                "text_id": "dialogue.option.town_inn_no",
                "next": "town inn no",
            },
        },
    },

    "town inn no": {
        "text_id": "dialogue.town_inn_no",
        "next": "town choice",
    },

    "town inn payment": {
        "text_id": "dialogue.town_inn_yes",
        "actions": [
            {
                "type": "check_coins",
                "value": 10,
                "if_pass": "town inn yes",
                "if_fail": "town inn low funds",
            }
        ]
    },

    "town inn low funds": {
        "text_id": "dialogue.town_inn_low_funds",
        "next": "town choice",
    },

    "town inn yes": {
        "text_id": "dialogue.town_inn_yes_2",
        "next": "town inn yes 2",
        "actions": [
            {
                "type": "set_flag",
                "target": "room_rented",
                "value": True,
            },
            {
                "type": "spend_coins",
                "value": 10,
            }
        ],
    },

    "town inn yes 2": {
        "text_id": "dialogue.town_inn_yes_3",
        "next": "inn bed options",
    },

    "inn bed options": {
        "text_id": "dialogue.bed_options",
        "options": {
            1: {
                "text_id": "dialogue.option.save_game",
                "next": "inn save game",
            },
            2: {
                "text_id": "dialogue.option.rest_in_bed",
                "next": "inn rest bed",
            },
            3: {
                "text_id": "dialogue.option.do_nothing",
                "next": "town choice",
            },
            4: {
                "text_id": "dialogue.option.main_menu",
                "next": "inn main menu",
            },
        },
    },

    "inn rest bed": {
        "text_id": "dialogue.rest_bed",
        "next": "inn restore bed",
    },

    "inn restore bed": {
        "text_id": "dialogue.restore_bed",
        "next": "inn wake",
        "actions": [
            {
                "type": "restore_health",
                "target": "full",
                "value": 100,
            },
        ],
    },

    "inn wake": {
        "text_id": "dialogue.town_inn_wake",
        "next": "town choice",
    },

    "inn save game": {
        "text_id": "dialogue.save_game",
        "options": {
            1: {
                "text_id": "dialogue.option.save_game_yes",
                "next": "inn save game yes",
            },
            2: {
                "text_id": "dialogue.option.save_game_no",
                "next": "inn save game no",
            },
            3: {
                "text_id": "dialogue.option.do_nothing",
                "next": "town choice",
            },
            4: {
                "text_id": "dialogue.option.main_menu",
                "next": "inn main menu",
            },
        },
    },

    "inn save game yes": {
        "text_id": "dialogue.save_game_yes",
        "next": "inn rest bed",
        "actions": [
            {
                "type": "save_game",
                "target": "inn_bed"
            }
        ],
    },

    "inn save game no": {
        "text_id": "dialogue.save_game_no",
        "next": "inn bed options",
    },

    "inn main menu": {
        "text_id": "dialogue.main_menu",
        "options": {
            1: {
                "text_id": "dialogue.option.main_menu_yes",
                "next": "inn main menu yes",
            },
            2: {
                "text_id": "dialogue.option.main_menu_no",
                "next": "inn main menu no",
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "inn main menu",
            },
            4: {
                "text_id": "dialogue.option.do_nothing",
                "next": "town choice",
            },
        },
    },

    "inn main menu yes": {
        "text_id": "dialogue.main_menu_yes",
        "actions": [
            {
                "type": "main_menu",
            }
        ],
    },

    "inn main menu no": {
        "text_id": "dialogue.main_menu_no",
        "next": "inn bed options",
    },





    "town black market": {
        "text_id": "dialogue.town_black_market_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.town_black_market_fence",
                "next": "town fence",
            },
            2: {
                "text_id": "dialogue.option.town_black_market_witch",
                "next": "town witch check",
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "town black market",
            },
            4: {
                "text_id": "dialogue.option.town_black_market_return",
                "next": "town choice",
            },
        },
    },

    "town fence": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_flag",
                "target": "has_visited_fence",
                "value": True,
                "if_pass": "town fence return",
                "if_fail": "town fence 1",
            }
        ],
    },

    "town fence 1": {
        "text_id": "dialogue.town_fence_1",
        "next": "town fence 2",
    },

    "town fence 2": {
        "text_id": "dialogue.town_fence_2",
        "next": "town fence 3",
    },

    "town fence 3": {
        "text_id": "dialogue.town_fence_3",
        "next": "town fence choice",
        "actions": [
            {
                "type": "set_flag",
                "target": "has_visited_fence",
                "value": True,
            }
        ],
    },

    "town fence return": {
        "text_id": "dialogue.town_fence_return",
        "next": "town fence choice",
    },

    "town fence choice": {
        "text_id": "dialogue.town_fence_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.town_fence_yes",
                "next": "town fence yes",
            },
            2: {
                "text_id": "dialogue.option.town_fence_no",
                "next": "town fence no",
            },
        },
    },

    "town fence no": {
        "text_id": "dialogue.town_fence_no",
        "next": "town fence no response",
    },

    "town fence no response": {
        "text_id": "dialogue.town_fence_no_response",
        "next": "town black market",
    },

    "town fence yes": {
        "text_id": "dialogue.town_fence_yes",
        "next": "town fence sell",
    },

    "town fence sell": {
        "text_id": "dialogue.town_fence_yes",
        "actions": [
            {
                "type": "sell_items",
                "target": "black_market_fence",
                "if_pass": "town fence sold",
                "if_fail": "town fence nothing",
            }
        ],
    },

    "town fence sold": {
        "text_id": "dialogue.town_fence_sold",
        "next": "town fence complete",
        "variables": {},
    },

    "town fence complete": {
        "text_id": "dialogue.town_fence_complete",
        "next": "town black market",
    },

    "town fence nothing": {
        "text_id": "dialogue.town_fence_nothing",
        "next": "town black market",
    },

    "town witch check": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_flag",
                "target": "met_witch",
                "value": True,
                "if_pass": "town witch choice",
                "if_fail": "town witch intro 1",
            }
        ]
    },

    "town witch intro 1": {
        "text_id": "dialogue.town_witch_intro_1",
        "next": "town witch intro 2",
    },

    "town witch intro 2": {
        "text_id": "dialogue.town_witch_intro_2",
        "next": "town witch choice",
        "actions": [
            {
                "type": "set_flag",
                "target": "met_witch",
                "value": True,
            }
        ]
    },

    "town witch choice": {
        "text_id": "dialogue.town_witch_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.town_witch_potions",
                "next": "town witch options choice",
            },            
            2: {
                "text_id": "dialogue.option.town_witch_bones",
                "next": "town witch bones check",
            },
            3: {
                "text_id": "dialogue.option.town_witch_explain",
                "next": "town witch explain 1",
            },
            4: {
                "text_id": "dialogue.option.town_witch_return",
                "next": "town black market",
            }
        }
    },


    "town witch options choice": {
        "text_id": "dialogue.town_witch_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.town_witch_rare",
                "next": "town witch rare ingredient check",
            },            
            2: {
                "text_id": "dialogue.option.town_witch_strange",
                "next": "town witch strange herb check",
            },
            3: {
                "text_id": "dialogue.option.town_witch_explain",
                "next": "town witch explain 1",
            },
            4: {
                "text_id": "dialogue.option.town_witch_return",
                "next": "town black market",
            }
        }
    },

    "town witch explain 1": {
        "text_id": "dialogue.town_witch_explain_1",
        "next": "town witch explain 2",
    },

    "town witch explain 2": {
        "text_id": "dialogue.town_witch_explain_2",
        "next": "town witch explain 3",
    },

    "town witch explain 3": {
        "text_id": "dialogue.town_witch_explain_3",
        "next": "town witch choice",
    },

    # Rare Potion
    "town witch rare ingredient check": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_items",
                "target": "Rare Ingredient",
                "value": 1,
                "if_pass": "town witch rare mushroom check",
                "if_fail": "town witch rare missing",
            }
        ]
    },

    "town witch rare mushroom check": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_items",
                "target": "Cave Mushroom",
                "value": 5,
                "if_pass": "town witch rare coins check",
                "if_fail": "town witch rare missing",
            }
        ]
    },

    "town witch rare coins check": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_coins",
                "value": 1000,
                "if_pass": "town witch rare 1",
                "if_fail": "town witch coins missing",
            }
        ]
    },


    "town witch rare missing": {
        "text_id": "dialogue.town_witch_rare_missing",
        "next": "town witch choice",
    },

    "town witch rare 1": {
        "text_id": "dialogue.town_witch_rare_1",
        "next": "town witch rare 2",
        "actions": [
            {
                "type": "spend_coins",
                "value": 1000,
            }
        ]
    },

    "town witch rare 2": {
        "text_id": "dialogue.town_witch_stir",
        "next": "town witch rare 3",
    },

    "town witch rare 3": {
        "text_id": "dialogue.town_witch_blue",
        "next": "town witch rare 4",
    },

    "town witch rare 4": {
        "text_id": "dialogue.town_witch_bottle",
        "next": "town witch rare 5",
    },

    "town witch rare 5": {
        "text_id": "dialogue.town_witch_drink",
        "actions": [
            {
                "type": "exchange_power",
                "target": "Rare Potion",
                "next": "town witch rare result",
            }
        ]
    },

    "town witch rare result": {
        "text_id": "dialogue.town_witch_power_3",
        "next": "town witch goodbye",
    },

    # Strange Potion
    "town witch strange herb check": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_items",
                "target": "Strange Herb",
                "value": 1,
                "if_pass": "town witch strange mushroom check",
                "if_fail": "town witch strange missing",
            }
        ]
    },

    "town witch strange mushroom check": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_items",
                "target": "Cave Mushroom",
                "value": 5,
                "if_pass": "town witch strange coins check",
                "if_fail": "town witch strange missing",
            }
        ]
    },

    "town witch strange coins check": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_coins",
                "value": 100,
                "if_pass": "town witch strange 1",
                "if_fail": "town witch coins missing",
            }
        ]
    },

    "town witch strange missing": {
        "text_id": "dialogue.town_witch_strange_missing",
        "next": "town witch choice",
    },

    "town witch coins missing": {
        "text_id": "dialogue.town_witch_coins_missing",
        "next": "town witch choice",
    },

    "town witch strange 1": {
        "text_id": "dialogue.town_witch_strange_1",
        "next": "town witch strange 2",
        "actions": [
            {
                "type": "spend_coins",
                "value": 100, 
            }
        ]
    },

    "town witch strange 2": {
        "text_id": "dialogue.town_witch_stir",
        "next": "town witch strange 3",
    },

    "town witch strange 3": {
        "text_id": "dialogue.town_witch_green",
        "next": "town witch strange 4",
    },

    "town witch strange 4": {
        "text_id": "dialogue.town_witch_bottle",
        "next": "town witch strange 5",
    },

    "town witch strange 5": {
        "text_id": "dialogue.town_witch_drink",
        "actions": [
            {
                "type": "exchange_power",
                "target": "Strange Potion",
                "next": "town witch strange result",
            }
        ]
    },

    "town witch strange result": {
        "text_id": "dialogue.town_witch_power_1",
        "next": "town witch goodbye",
    },

    # Bone Ritual
    "town witch bones check": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_items",
                "target": "Bones",
                "value": 25,
                "if_pass": "town witch bones 1",
                "if_fail": "town witch bones missing",
            }
        ]
    },

    "town witch bones missing": {
        "text_id": "dialogue.town_witch_bones_missing",
        "next": "town witch choice",
    },

    "town witch bones 1": {
        "text_id": "dialogue.town_witch_bones_1",
        "next": "town witch bones 2",
    },

    "town witch bones 2": {
        "text_id": "dialogue.town_witch_bones_2",
        "next": "town witch bones 3",
    },

    "town witch bones 3": {
        "text_id": "dialogue.town_witch_bones_3",
        "actions": [
            {
                "type": "exchange_power",
                "target": "Bones",
                "next": "town witch bones result",
            }
        ]
    },

    "town witch bones result": {
        "text_id": "dialogue.town_witch_power_1",
        "next": "town witch goodbye",
    },

    "town witch goodbye": {
        "text_id": "dialogue.town_witch_goodbye",
        "next": "town witch choice",
    },



    # BS

    "town blacksmith": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_flag",
                "target": "has_visited_blacksmith",
                "value": True,
                "if_pass": "town blacksmith return",
                "if_fail": "town blacksmith 1",
            }
        ]
    },


    "town blacksmith 1": {
        "text_id": "dialogue.town_blacksmith_1",
        "next": "town blacksmith 2",
        "actions": [
            {
                "type": "set_flag",
                "target": "has_visited_blacksmith",
                "value": True,
            }
        ]
    },

    "town blacksmith 2": {
        "text_id": "dialogue.town_blacksmith_2",
        "next": "town blacksmith 3",
    },

    "town blacksmith 3": {
        "text_id": "dialogue.town_blacksmith_3",
        "next": "town blacksmith 4",
    },

    "town blacksmith 4": {
        "text_id": "dialogue.town_blacksmith_4",
        "next": "town blacksmith 5",
    },

    "town blacksmith 5": {
        "text_id": "dialogue.town_blacksmith_5",
        "next": "town blacksmith 6",
    },

    "town blacksmith 6": {
        "text_id": "dialogue.town_blacksmith_6",
        "next": "town blacksmith 7",
    },

    "town blacksmith 7": {
        "text_id": "dialogue.town_blacksmith_7",
        "next": "town blacksmith 8",
    },

    "town blacksmith 8": {
        "text_id": "dialogue.town_blacksmith_8",
        "next": "town blacksmith 9",
    },

    "town blacksmith 9": {
        "text_id": "dialogue.town_blacksmith_9",
        "next": "town blacksmith 10",
    },

    "town blacksmith 10": {
        "text_id": "dialogue.town_blacksmith_10",
        "next": "town vendors choice",
    },



    "town blacksmith return": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_flag",
                "target": "reaper_knowledge",
                "value": True,
                "if_pass": "town blacksmith technique check",
                "if_fail": "town blacksmith return 1",
            }
        ]
    },


    "town blacksmith return 1": {
        "text_id": "dialogue.town_blacksmith_return_1",
        "next": "town blacksmith return 2",
    },

    "town blacksmith return 2": {
        "text_id": "dialogue.town_blacksmith_return_2",
        "next": "town blacksmith return 3",
    },

    "town blacksmith return 3": {
        "text_id": "dialogue.town_blacksmith_return_3",
        "next": "town blacksmith return 4",
    },

    "town blacksmith return 4": {
        "text_id": "dialogue.town_blacksmith_return_4",
        "next": "town vendors choice",
    },


    "town blacksmith technique check": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_flag",
                "target": "ancient_technique_shared",
                "value": True,
                "if_pass": "town blacksmith crafting unlock check",
                "if_fail": "town blacksmith knowledge 1",
            }
        ]
    },



    "town blacksmith knowledge 1": {
        "text_id": "dialogue.town_blacksmith_return_1",
        "next": "town blacksmith knowledge 2",
    },

    "town blacksmith knowledge 2": {
        "text_id": "dialogue.town_blacksmith_knowledge_1",
        "next": "town blacksmith knowledge 3",
    },

    "town blacksmith knowledge 3": {
        "text_id": "dialogue.town_blacksmith_knowledge_2",
        "next": "town blacksmith knowledge 4",
    },

    "town blacksmith knowledge 4": {
        "text_id": "dialogue.town_blacksmith_knowledge_3",
        "next": "town blacksmith knowledge 5",
    },

    "town blacksmith knowledge 5": {
        "text_id": "dialogue.town_blacksmith_knowledge_4",
        "next": "town blacksmith knowledge 6",
    },

    "town blacksmith knowledge 6": {
        "text_id": "dialogue.town_blacksmith_knowledge_5",
        "next": "town blacksmith knowledge 7",
    },

    "town blacksmith knowledge 7": {
        "text_id": "dialogue.town_blacksmith_knowledge_6",
        "next": "town blacksmith knowledge 8",
    },

    "town blacksmith knowledge 8": {
        "text_id": "dialogue.town_blacksmith_knowledge_7",
        "next": "town blacksmith knowledge 9",
    },

    "town blacksmith knowledge 9": {
        "text_id": "dialogue.town_blacksmith_knowledge_8",
        "next": "town blacksmith knowledge 10",
    },

    "town blacksmith knowledge 10": {
        "text_id": "dialogue.town_blacksmith_knowledge_9",
        "next": "town blacksmith knowledge 11",
    },

    "town blacksmith knowledge 11": {
        "text_id": "dialogue.town_blacksmith_knowledge_10",
        "next": "town blacksmith knowledge 12",
    },

    "town blacksmith knowledge 12": {
        "text_id": "dialogue.town_blacksmith_knowledge_11",
        "next": "town blacksmith knowledge 13",
    },

    "town blacksmith knowledge 13": {
        "text_id": "dialogue.town_blacksmith_knowledge_12",
        "next": "town blacksmith knowledge 14",
    },

    "town blacksmith knowledge 14": {
        "text_id": "dialogue.town_blacksmith_knowledge_13",
        "next": "town blacksmith knowledge 15",
    },

    "town blacksmith knowledge 15": {
        "text_id": "dialogue.town_blacksmith_knowledge_14",
        "next": "town blacksmith knowledge 16",
    },

    "town blacksmith knowledge 16": {
        "text_id": "dialogue.town_blacksmith_knowledge_15",
        "next": "town blacksmith knowledge 17",
    },

    "town blacksmith knowledge 17": {
        "text_id": "dialogue.town_blacksmith_knowledge_16",
        "next": "town blacksmith knowledge 18",
    },

    "town blacksmith knowledge 18": {
        "text_id": "dialogue.town_blacksmith_knowledge_17",
        "next": "town blacksmith knowledge 19",
    },

    "town blacksmith knowledge 19": {
        "text_id": "dialogue.town_blacksmith_knowledge_18",
        "next": "town blacksmith knowledge 20",
    },

    "town blacksmith knowledge 20": {
        "text_id": "dialogue.town_blacksmith_knowledge_19",
        "next": "town blacksmith knowledge 21",
    },

    "town blacksmith knowledge 21": {
        "text_id": "dialogue.town_blacksmith_knowledge_20",
        "next": "town blacksmith knowledge 22",
    },

    "town blacksmith knowledge 22": {
        "text_id": "dialogue.town_blacksmith_knowledge_21",
        "next": "town blacksmith knowledge 23",
    },

    "town blacksmith knowledge 23": {
        "text_id": "dialogue.town_blacksmith_knowledge_22",
        "next": "town blacksmith knowledge 24",
    },

    "town blacksmith knowledge 24": {
        "text_id": "dialogue.town_blacksmith_knowledge_23",
        "next": "town blacksmith knowledge 25",
        "actions": [
            {
                "type": "earn_coins",
                "value": 100,
            }
        ]
    },

    "town blacksmith knowledge 25": {
        "text_id": "dialogue.town_blacksmith_knowledge_24",
        "next": "town blacksmith knowledge 26",
    },

    "town blacksmith knowledge 26": {
        "text_id": "dialogue.town_blacksmith_knowledge_25",
        "next": "town blacksmith knowledge 27",
    },

    "town blacksmith knowledge 27": {
        "text_id": "dialogue.town_blacksmith_knowledge_26",
        "next": "town blacksmith knowledge 28",
    },

    "town blacksmith knowledge 28": {
        "text_id": "dialogue.town_blacksmith_knowledge_27",
        "next": "town blacksmith knowledge 29",
    },

    "town blacksmith knowledge 29": {
        "text_id": "dialogue.town_blacksmith_knowledge_28",
        "next": "town blacksmith knowledge 30",
    },

    "town blacksmith knowledge 30": {
        "text_id": "dialogue.town_blacksmith_knowledge_29",
        "next": "town vendors choice",
        "actions": [
            {
                "type": "set_flag",
                "target": "ancient_technique_shared",
                "value": True,
            }
        ]
    },



    "town blacksmith crafting unlock check": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_flag",
                "target": "ancient_crafting_unlocked",
                "value": True,
                "if_pass": "town blacksmith craft return check",
                "if_fail": "town blacksmith armament check",
            }
        ]
    },

    "town blacksmith armament check": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_items",
                "target": "Ancient Armament",
                "value": 1,
                "if_pass": "town blacksmith armament 1",
                "if_fail": "town blacksmith armament none 1",
            }
        ]
    },

    # No Ancient Armament yet
    "town blacksmith armament none 1": {
        "text_id": "dialogue.town_blacksmith_armament_1",
        "next": "town blacksmith armament none 2",
    },

    "town blacksmith armament none 2": {
        "text_id": "dialogue.town_blacksmith_nothing_1",
        "next": "town blacksmith armament none 3",
    },

    "town blacksmith armament none 3": {
        "text_id": "dialogue.town_blacksmith_nothing_2",
        "next": "town vendors choice",
    },



    "town blacksmith armament 1": {
        "text_id": "dialogue.town_blacksmith_armament_1",
        "next": "town blacksmith armament 2",
    },

    "town blacksmith armament 2": {
        "text_id": "dialogue.town_blacksmith_armament_2",
        "next": "town blacksmith armament 3",
    },

    "town blacksmith armament 3": {
        "text_id": "dialogue.town_blacksmith_armament_3",
        "next": "town blacksmith armament 4",
    },

    "town blacksmith armament 4": {
        "text_id": "dialogue.town_blacksmith_armament_4",
        "next": "town blacksmith armament 5",
    },

    "town blacksmith armament 5": {
        "text_id": "dialogue.town_blacksmith_armament_5",
        "next": "town blacksmith armament 6",
    },

    "town blacksmith armament 6": {
        "text_id": "dialogue.town_blacksmith_armament_6",
        "next": "town blacksmith armament 7",
    },

    "town blacksmith armament 7": {
        "text_id": "dialogue.town_blacksmith_armament_7",
        "next": "town blacksmith armament 8",
    },

    "town blacksmith armament 8": {
        "text_id": "dialogue.town_blacksmith_armament_8",
        "next": "town blacksmith armament 9",
    },

    "town blacksmith armament 9": {
        "text_id": "dialogue.town_blacksmith_armament_9",
        "next": "town blacksmith armament 10",
    },

    "town blacksmith armament 10": {
        "text_id": "dialogue.town_blacksmith_armament_10",
        "next": "town blacksmith armament 11",
    },

    "town blacksmith armament 11": {
        "text_id": "dialogue.town_blacksmith_armament_11",
        "next": "town blacksmith armament 12",
    },

    "town blacksmith armament 12": {
        "text_id": "dialogue.town_blacksmith_armament_12",
        "next": "town blacksmith armament 13",
    },

    "town blacksmith armament 13": {
        "text_id": "dialogue.town_blacksmith_armament_13",
        "next": "town blacksmith armament 14",
    },

    "town blacksmith armament 14": {
        "text_id": "dialogue.town_blacksmith_armament_14",
        "next": "town blacksmith craft check",
        "actions": [
            {
                "type": "set_flag",
                "target": "ancient_crafting_unlocked",
                "value": True,
            }
        ]
    },

    "town blacksmith craft return check": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_flag",
                "target": "ancient_armor_crafted",
                "value": True,
                "if_pass": "town blacksmith craft return check 2",
                "if_fail": "town blacksmith craft return",
            }
        ]
    },

    "town blacksmith craft return check 2": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_flag",
                "target": "ancient_weapon_crafted",
                "value": True,
                "if_pass": "town blacksmith complete return 1",
                "if_fail": "town blacksmith craft return",
            }
        ]
    },




    "town blacksmith craft return": {
        "text_id": "dialogue.town_blacksmith_craft_return",
        "next": "town blacksmith craft check",
    },

    "town blacksmith complete return 1": {
        "text_id": "dialogue.town_blacksmith_complete_return_1",
        "next": "town blacksmith complete return 2",
    },

    "town blacksmith complete return 2": {
        "text_id": "dialogue.town_blacksmith_complete_return_2",
        "next": "town vendors choice",
    },


    # BLACKSMITH CRAFTING STATE CHECKS

    # First check whether the weapon has been crafted.
    "town blacksmith craft check": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_flag",
                "target": "ancient_weapon_crafted",
                "value": True,
                "if_pass": "town blacksmith craft check weapon true",
                "if_fail": "town blacksmith craft check weapon false",
            }
        ]
    },

    # Weapon IS crafted.
    # Now determine whether armor is also crafted.
    "town blacksmith craft check weapon true": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_flag",
                "target": "ancient_armor_crafted",
                "value": True,
                "if_pass": "town blacksmith complete 1",
                "if_fail": "town blacksmith craft armor only",
            }
        ]
    },

    # Weapon is NOT crafted.
    # Now determine whether armor has been crafted.
    "town blacksmith craft check weapon false": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_flag",
                "target": "ancient_armor_crafted",
                "value": True,
                "if_pass": "town blacksmith craft weapon only",
                "if_fail": "town blacksmith craft choice",
            }
        ]
    },


    "town blacksmith craft choice": {
        "text_id": "dialogue.town_blacksmith_craft_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.town_blacksmith_armor",
                "next": "town blacksmith armor coin check",
            },
            2: {
                "text_id": "dialogue.option.town_blacksmith_weapon",
                "next": "town blacksmith weapon coin check",
            },
            3: {
                "text_id": "dialogue.option.town_blacksmith_nothing",
                "next": "town blacksmith nothing 1",
            },
            4: {
                "text_id": "dialogue.option.town_choice",
                "next": "town vendors choice",
            },
        }
    },

    "town blacksmith nothing 1": {
        "text_id": "dialogue.town_blacksmith_nothing_1",
        "next": "town blacksmith nothing 2",
    },

    "town blacksmith nothing 2": {
        "text_id": "dialogue.town_blacksmith_nothing_2",
        "next": "town vendors choice",
    },



    "town blacksmith craft weapon only": {
        "text_id": "dialogue.town_blacksmith_craft_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.town_blacksmith_weapon",
                "next": "town blacksmith weapon coin check",
            },
            2: {
                "text_id": "dialogue.empty",
                "next": "town blacksmith craft weapon only",
            },
            3: {
                "text_id": "dialogue.empty",
                "next": "town blacksmith craft weapon only",
            },
            4: {
                "text_id": "dialogue.option.town_blacksmith_nothing",
                "next": "town blacksmith nothing 1",
            },
        }
    },


    "town blacksmith craft armor only": {
        "text_id": "dialogue.town_blacksmith_craft_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.town_blacksmith_armor",
                "next": "town blacksmith armor coin check",
            },
            2: {
                "text_id": "dialogue.empty",
                "next": "town blacksmith craft armor only",
            },
            3: {
                "text_id": "dialogue.empty",
                "next": "town blacksmith craft armor only",
            },
            4: {
                "text_id": "dialogue.option.town_blacksmith_nothing",
                "next": "town blacksmith nothing 1",
            },
        }
    },




    "town blacksmith armor coin check": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_coins",
                "value": 500,
                "if_pass": "town blacksmith armor armament check",
                "if_fail": "town blacksmith no gold 1",
            }
        ]
    },


    "town blacksmith armor armament check": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_items",
                "target": "Ancient Armament",
                "value": 4,
                "if_pass": "town blacksmith armor 1",
                "if_fail": "town blacksmith no armor 1",
            }
        ]
    },

    "town blacksmith no gold 1": {
        "text_id": "dialogue.town_blacksmith_no_gold_1",
        "next": "town blacksmith no gold 2",
    },

    "town blacksmith no gold 2": {
        "text_id": "dialogue.town_blacksmith_no_gold_2",
        "next": "town blacksmith craft choice",
    },

    "town blacksmith no armor 1": {
        "text_id": "dialogue.town_blacksmith_no_armor_1",
        "next": "town blacksmith no armor 2",
    },

    "town blacksmith no armor 2": {
        "text_id": "dialogue.town_blacksmith_no_armor_2",
        "next": "town blacksmith craft choice",
    },

    "town blacksmith armor 1": {
        "text_id": "dialogue.town_blacksmith_armor_1",
        "next": "town blacksmith armor 2",
    },

    "town blacksmith armor 2": {
        "text_id": "dialogue.town_blacksmith_armor_2",
        "next": "town blacksmith armor 3",
    },


    "town blacksmith armor 3": {
        "text_id": "dialogue.town_blacksmith_armor_3",
        "next": "town blacksmith armor 4",
        "actions": [
            {
                "type": "spend_coins",
                "value": 500,
            }
        ]
    },

    "town blacksmith armor 4": {
        "text_id": "dialogue.town_blacksmith_armor_4",
        "next": "town blacksmith armor forge 1",
    },

    "town blacksmith armor forge 1": {
        "text_id": "dialogue.town_blacksmith_forge_1",
        "next": "town blacksmith armor forge 2",
    },

    "town blacksmith armor forge 2": {
        "text_id": "dialogue.town_blacksmith_forge_2",
        "next": "town blacksmith armor forge 3",
    },

    "town blacksmith armor forge 3": {
        "text_id": "dialogue.town_blacksmith_forge_3",
        "next": "town blacksmith armor forge 4",
    },

    "town blacksmith armor forge 4": {
        "text_id": "dialogue.town_blacksmith_forge_4",
        "next": "town blacksmith armor complete 1",
    },

    "town blacksmith armor complete 1": {
        "text_id": "dialogue.town_blacksmith_armor_complete_1",
        "next": "town blacksmith armor complete 2",
    },

    "town blacksmith armor complete 2": {
        "text_id": "dialogue.town_blacksmith_armor_complete_2",
        "next": "town blacksmith armor complete 3",
    },

    "town blacksmith armor complete 3": {
        "text_id": "dialogue.town_blacksmith_armor_complete_3",
        "next": "town blacksmith armor complete 4",
    },

    "town blacksmith armor complete 4": {
        "text_id": "dialogue.town_blacksmith_armor_complete_4",
        "next": "town blacksmith armor complete 5",
        "actions": [
            {
                "type": "set_flag",
                "target": "ancient_armor_crafted",
                "value": True,
            }
        ]
    },

 
    "town blacksmith armor complete 5": {
        "text_id": "dialogue.town_blacksmith_armor_complete_5",
        "next": "town blacksmith craft check",
        "actions": [
            {
                "type": "exchange_armament",
                "target": "blacksmith armor",
            }
        ]
    },



    "town blacksmith weapon coin check": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_coins",
                "value": 300,
                "if_pass": "town blacksmith weapon armament check",
                "if_fail": "town blacksmith no gold 1",
            }
        ]
    },


    "town blacksmith weapon armament check": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_items",
                "target": "Ancient Armament",
                "value": 2,
                "if_pass": "town blacksmith weapon 1",
                "if_fail": "town blacksmith no weapon 1",
            }
        ]
    },

    "town blacksmith no weapon 1": {
        "text_id": "dialogue.town_blacksmith_no_weapon_1",
        "next": "town blacksmith no weapon 2",
    },

    "town blacksmith no weapon 2": {
        "text_id": "dialogue.town_blacksmith_no_weapon_2",
        "next": "town blacksmith craft choice",
    },

    "town blacksmith weapon 1": {
        "text_id": "dialogue.town_blacksmith_weapon_1",
        "next": "town blacksmith weapon 2",
    },

    "town blacksmith weapon 2": {
        "text_id": "dialogue.town_blacksmith_weapon_2",
        "next": "town blacksmith weapon 3",
    },


    "town blacksmith weapon 3": {
        "text_id": "dialogue.town_blacksmith_weapon_3",
        "next": "town blacksmith weapon 4",
        "actions": [
            {
                "type": "spend_coins",
                "value": 300,
            }
        ]
    },

    "town blacksmith weapon 4": {
        "text_id": "dialogue.town_blacksmith_weapon_4",
        "next": "town blacksmith weapon forge 1",
    },

    "town blacksmith weapon forge 1": {
        "text_id": "dialogue.town_blacksmith_forge_1",
        "next": "town blacksmith weapon forge 2",
    },

    "town blacksmith weapon forge 2": {
        "text_id": "dialogue.town_blacksmith_forge_2",
        "next": "town blacksmith weapon forge 3",
    },

    "town blacksmith weapon forge 3": {
        "text_id": "dialogue.town_blacksmith_forge_3",
        "next": "town blacksmith weapon forge 4",
    },

    "town blacksmith weapon forge 4": {
        "text_id": "dialogue.town_blacksmith_forge_4",
        "next": "town blacksmith weapon complete 1",
    },

    "town blacksmith weapon complete 1": {
        "text_id": "dialogue.town_blacksmith_weapon_complete_1",
        "next": "town blacksmith weapon complete 2",
    },

    "town blacksmith weapon complete 2": {
        "text_id": "dialogue.town_blacksmith_weapon_complete_2",
        "next": "town blacksmith weapon complete 3",
    },

    "town blacksmith weapon complete 3": {
        "text_id": "dialogue.town_blacksmith_weapon_complete_3",
        "next": "town blacksmith weapon complete 4",
    },

    "town blacksmith weapon complete 4": {
        "text_id": "dialogue.town_blacksmith_weapon_complete_4",
        "next": "town blacksmith weapon complete 5",
        "actions": [
            {
                "type": "set_flag",
                "target": "ancient_weapon_crafted",
                "value": True,
            }
        ]
    },


    "town blacksmith weapon complete 5": {
        "text_id": "dialogue.town_blacksmith_weapon_complete_5",
        "next": "town blacksmith craft check",
        "actions": [
            {
                "type": "exchange_armament",
                "target": "blacksmith weapon",
            }
        ]
    },

    "town blacksmith weapon finish": {
        "text_id": "dialogue.empty",
        "next": "town blacksmith craft check",
        "actions": [
            {
                "type": "set_flag",
                "target": "ancient_weapon_crafted",
                "value": True,
            }
        ]
    },


    "town blacksmith complete 1": {
        "text_id": "dialogue.town_blacksmith_complete_1",
        "next": "town blacksmith complete 2",
    },

    "town blacksmith complete 2": {
        "text_id": "dialogue.town_blacksmith_complete_2",
        "next": "town blacksmith complete 3",
    },

    "town blacksmith complete 3": {
        "text_id": "dialogue.town_blacksmith_complete_3",
        "next": "town blacksmith complete 4",
    },

    "town blacksmith complete 4": {
        "text_id": "dialogue.town_blacksmith_complete_4",
        "next": "town vendors choice",
    },




    "town specialty": {
        "text_id": "dialogue.town_specialty_1",
        "next": "town specialty 2"
    },

    "town specialty 2": {
        "text_id": "dialogue.town_specialty_2",
        "next": "town specialty 3"
    },

    "town specialty 3": {
        "text_id": "dialogue.town_specialty_3",
        "next": "town specialty choice"
    },

    "town specialty choice": {
        "text_id": "dialogue.town_specialty_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.town_specialty_armaments",
                "next": "town specialty armament check"
            },
            2: {
                "text_id": "dialogue.option.town_specialty_crystals",
                "next": "town specialty crystal check"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "town specialty choice"
            },
            4: {
                "text_id": "dialogue.option.town_specialty_nothing",
                "next": "town specialty no"
            }
        }
    },

    "town specialty no": {
        "text_id": "dialogue.town_specialty_no",
        "next": "town vendors choice"
    },

    "town specialty armament check": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_items",
                "target": "Ancient Armament",
                "value": 1,
                "if_pass": "town specialty exchange 1",
                "if_fail": "town specialty none",
            }
        ]
    },

    "town specialty exchange 1": {
        "text_id": "dialogue.town_specialty_exchange_1",
        "next": "town specialty exchange 2"
    },

    "town specialty exchange 2": {
        "text_id": "dialogue.town_specialty_exchange_2",
        "actions": [
            {
                "type": "exchange_power",
                "target": "Ancient Armament",
                "next": "town specialty exchange 3"
            }
        ]
    },

    "town specialty exchange 3": {
        "text_id": "dialogue.town_specialty_exchange_3",
        "next": "town specialty 4",
        "variables": {
            "count": 0,
            "power": 0
        }
    },

    "town specialty crystal check": {
        "text_id": "dialogue.empty",
        "actions": [
            {
                "type": "check_items",
                "target": "Crystal Fragment",
                "value": 10,
                "if_pass": "town specialty crystal 1",
                "if_fail": "town specialty crystal none",
            }
        ]
    },

    "town specialty crystal none": {
        "text_id": "dialogue.town_specialty_crystal_none",
        "next": "town specialty choice"
    },

    "town specialty crystal 1": {
        "text_id": "dialogue.town_specialty_crystal_1",
        "next": "town specialty crystal 2"
    },

    "town specialty crystal 2": {
        "text_id": "dialogue.town_specialty_crystal_2",
        "next": "town specialty crystal 3"
    },

    "town specialty crystal 3": {
        "text_id": "dialogue.town_specialty_crystal_3",
        "next": "town specialty crystal 4"
    },

    "town specialty crystal 4": {
        "text_id": "dialogue.town_specialty_crystal_4",
        "actions": [
            {
                "type": "exchange_power",
                "target": "Crystal Fragment",
                "next": "town specialty crystal 5"
            }
        ]
    },

    "town specialty crystal 5": {
        "text_id": "dialogue.town_specialty_crystal_5",
        "next": "town specialty 4",
        "variables": {
            "count": 0,
            "power": 0
        }
    },

    "town specialty none": {
        "text_id": "dialogue.town_specialty_none",
        "next": "town specialty choice"
    },

    "town specialty 4": {
        "text_id": "dialogue.town_specialty_4",
        "next": "town vendors choice"
    },




    "town sewer 1": {
        "text_id": "dialogue.town_sewer_1",
        "next": "town sewer 2"
    },

    "town sewer 2": {
        "text_id": "dialogue.town_sewer_2",
        "next": "sewer secret return"
    },

    "sewer secret return": {
        "text_id": "dialogue.return_to_sewer_2",
        "next": "sewer choice",
        "actions": [
            {   
                "type": "map",
                "target": "sewer"
            }
        ]
    },


    "town 3": {
        "text_id": "dialogue.town_3",
        "next": "town 4"
    },

    "town 4": {
        "text_id": "dialogue.town_4",
        "next": "town 5"
    },

    "town 5": {
        "text_id": "dialogue.town_5",
        "next": "enter crypt 1"
    },

    "enter crypt 1": {
        "text_id": "dialogue.enter_crypt_1",
        "next": "crypt 1 main check",
        "actions": [
            {   
                "type": "map",
                "target": "crypt 1"
            }
        ]
    },

    "crypt 1 main check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "crypt_1_empty",
                "value": True,
                "if_pass": "crypt 1 intro B",
                "if_fail": "crypt 1 intro",
            }
        ]
    },

    "crypt 1 intro B": {
        "text_id": "dialogue.crypt_1_intro_b",
        "next": "crypt 1 choice"
    },

    "crypt 1 intro": {
        "text_id": "dialogue.crypt_1_intro",
        "next": "crypt 1 cont"
    },

    "crypt 1 cont": {
        "text_id": "dialogue.crypt_1_cont",
        "next": "crypt 1 choice"
    },


    "crypt 1 choice": {
        "text_id": "dialogue.crypt_1_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.crypt_1_explore",
                "next": "crypt 1 explore 1"
            },
            2: {
                "text_id": "dialogue.option.crypt_1_enemies",
                "next": "crypt 1 enemies choice"
            },
            3: {
                "text_id": "dialogue.option.crypt_1_continue",
                "next": "crypt 1 continue"
            },
            4: {
                "text_id": "dialogue.option.crypt_1_return",
                "next": "town return"
            }
        }
    },

    "crypt 1 explore 1": {
        "text_id": "dialogue.crypt_1_explore_1",
        "actions": [
            {   
                "type": "check_flag",
                "target": "crypt_1_empty",
                "value": False,
                "if_pass": "crypt 1 explore start",
                "if_fail": "reaper knowledge check",
            }
        ]
    },


    "crypt 1 explore start": {
        "text_id": "dialogue.crypt_1_explore_2",
        "next": "crypt 1 choice",
        "actions": [
            {
                "type": "set_flag",
                "target": "crypt_1_empty",
                "value": True
            },
            {   
                "type": "explore_items",
                "target": "crypt_1",
            }
        ]
    },

    # check reaper_knowledge
    "reaper knowledge check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "reaper_knowledge",
                "value": True,
                "if_pass": "reaper choice check",
                "if_fail": "crypt 1 explore empty",
            }
        ]
    },


    "crypt 1 explore empty": {
        "text_id": "dialogue.crypt_1_explore_empty",
        "next": "crypt 1 choice",
    },

    # reaper path

    "reaper choice check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "reaper_choice_made",
                "value": False,
                "if_pass": "reaper ritual 1",
                "if_fail": "reaper deal check",
            }
        ]
    },

    "reaper deal check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "accepted_deal",
                "value": False,
                "if_pass": "reaper boss choice",
                "if_fail": "reaper lord defeated check",
            }
        ]
    },


    "reaper lord defeated check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "lord_defeated",
                "value": True,
                "if_pass": "reaper reward check",
                "if_fail": "reaper lord alive",
            }
        ]
    },

    "reaper lord alive": {
        "text_id": "dialogue.reaper_lord_alive",
        "next": "crypt 1 explore",
    },

    "reaper reward check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "reaper_reward_given",
                "value": False,
                "if_pass": "reaper lord reward",
                "if_fail": "reaper no response",
            }
        ]
    },


    "reaper no response": {
        "text_id": "dialogue.reaper_no_response",
        "next": "crypt 1 explore",
    },

    "reaper lord reward": {
        "text_id": "dialogue.reaper_lord_reward_1",
        "next": "reaper lord reward 2",
        "actions": [
            {
                "type": "set_flag",
                "target": "reaper_reward_given",
                "value": True
            },
            {   
                "type": "equip",
                "target": "Ring of Death",
                "slot": "ring",
                "value": 1
            }            
        ]
    },

    "reaper lord reward 2": {
        "text_id": "dialogue.reaper_lord_reward_2",
        "next": "crypt 1 choice",
    },


    "reaper ritual 1": {
        "text_id": "dialogue.reaper_ritual_1",
        "next": "reaper ritual 2",
    },

    "reaper ritual 2": {
        "text_id": "dialogue.reaper_ritual_2",
        "next": "reaper intro 1",
    },

    "reaper intro 1": {
        "text_id": "dialogue.reaper_intro_1",
        "next": "reaper intro 2",
    },

    "reaper intro 2": {
        "text_id": "dialogue.reaper_intro_2",
        "next": "reaper intro 3",
    },

    "reaper intro 3": {
        "text_id": "dialogue.reaper_intro_3",
        "next": "reaper paladin class check",
    },

    # check if paladin or not

    "reaper paladin class check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_class",
                "target": "Paladin",
                "if_pass": "reaper decline paladin",
                "if_fail": "reaper make choice",
            }
        ]
    },

    # choice accept or decline

    "reaper make choice": {
        "text_id": "dialogue.reaper_make_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.reaper_accept",
                "next": "reaper accept 1"
            },
            2: {
                "text_id": "dialogue.option.reaper_decline",
                "next": "reaper decline 1"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "reaper make choice"
            },
            4: {
                "text_id": "dialogue.option.empty",
                "next": "reaper make choice"
            }
        }
    },

    # accept 
    "reaper accept 1": {
        "text_id": "dialogue.reaper_accept_1",
        "next": "reaper accept 2",
        "actions": [
            {
                "type": "set_flag",
                "target": "reaper_choice_made",
                "value": True
            },
            {
                "type": "set_flag",
                "target": "accepted_deal",
                "value": True
            }
        ]
    },

    "reaper accept 2": {
        "text_id": "dialogue.reaper_accept_2",
        "next": "reaper accept 3"
    },

    "reaper accept 3": {
        "text_id": "dialogue.reaper_accept_3",
        "next": "reaper accept 4",
        "actions": [
            {
                "type": "set_class",
                "target": "Reaper",
                "value": True
            }
        ]
    },

    "reaper accept 4": {
        "text_id": "dialogue.reaper_accept_4",
        "next": "crypt 1 choice"
    },

    # consider adding more choices for backstory

    # decline paladin
    "reaper decline paladin": {
        "text_id": "dialogue.reaper_decline_paladin",
        "next": "reaper decline 2",
        "actions": [
            {
                "type": "set_flag",
                "target": "reaper_choice_made",
                "value": True
            },
            {
                "type": "set_flag",
                "target": "accepted_deal",
                "value": False
            }
        ]
    },

    # decline
    "reaper decline 1": {
        "text_id": "dialogue.reaper_decline_1",
        "next": "reaper decline 2",
        "actions": [
            {
                "type": "set_flag",
                "target": "reaper_choice_made",
                "value": True
            },
            {
                "type": "set_flag",
                "target": "accepted_deal",
                "value": False
            }
        ]
    },

    "reaper decline 2": {
        "text_id": "dialogue.reaper_decline_2",
        "next": "reaper decline 3"
    },

    "reaper decline 3": {
        "text_id": "dialogue.reaper_decline_3",
        "next": "reaper decline 4"
    },

    "reaper decline 4": {
        "text_id": "dialogue.reaper_decline_4",
        "next": "reaper boss choice"
    },

    "reaper boss choice": {
        "text_id": "dialogue.reaper_boss_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.reaper_boss_1",
                "next": "reaper boss 1"
            },
            2: {
                "text_id": "dialogue.option.reaper_boss_2",
                "next": "reaper boss 2"
            },
            3: {
                "text_id": "dialogue.option.reaper_boss_3",
                "next": "reaper boss 3"
            },
            4: {
                "text_id": "dialogue.option.reaper_boss_4",
                "next": "reaper boss 4"
            }
        }
    },

    "reaper boss 1": {
        "text_id": "dialogue.reaper_boss_victory",
        "next": "reaper boss victory",
        "actions": [
            {   
                "type": "encounter",
                "target": "reaper_boss_1",
            }
        ]
    },

    "reaper boss 2": {
        "text_id": "dialogue.reaper_boss_victory",
        "next": "reaper boss victory",
        "actions": [
            {   
                "type": "encounter",
                "target": "reaper_boss_2",
            }
        ]
    },

    "reaper boss 3": {
        "text_id": "dialogue.reaper_boss_victory",
        "next": "reaper boss victory",
        "actions": [
            {   
                "type": "encounter",
                "target": "reaper_boss_3",
            }
        ]
    },

    "reaper boss 4": {
        "text_id": "dialogue.reaper_boss_victory",
        "next": "reaper boss victory",
        "actions": [
            {   
                "type": "encounter",
                "target": "reaper_boss_4",
            }
        ]
    },

    "reaper boss victory": {
        "text_id": "dialogue.reaper_boss_victory_2",
        "next": "crypt 1 choice"
    },


    # reaper nodes end
    "crypt 1 enemies choice": {
        "text_id": "dialogue.crypt_1_enemies_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.crypt_1_enemies_1",
                "next": "crypt 1 enemies 1"
            },
            2: {
                "text_id": "dialogue.option.crypt_1_enemies_2",
                "next": "crypt 1 enemies 2"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "crypt 1 enemies choice"
            },
            4: {
                "text_id": "dialogue.option.crypt_1_do_nothing",
                "next": "crypt 1 choice"
            }
        }
    },


    "crypt 1 enemies 1": {
        "text_id": "dialogue.crypt_1_enemies_1",
        "next": "crypt 1 enemies 1 cont",
        "actions": [
            {   
                "type": "encounter",
                "target": "crypt_1_enemies_1",
            }
        ]
    },


    "crypt 1 enemies 1 cont": {
        "text_id": "dialogue.crypt_1_enemies_1_cont",
        "next": "crypt 1 choice",
    },


    "crypt 1 enemies 2": {
        "text_id": "dialogue.crypt_1_enemies_2",
        "next": "crypt 1 enemies 2 cont",
        "actions": [
            {   
                "type": "encounter",
                "target": "crypt_1_enemies_2",
            }
        ]
    },


    "crypt 1 enemies 2 cont": {
        "text_id": "dialogue.crypt_1_enemies_2_cont",
        "next": "crypt 1 choice",
    },





    "town return": {
        "text_id": "dialogue.return_to_town",
        "next": "town choice",
        "actions": [
            {   
                "type": "map",
                "target": "town"
            }
        ]
    },

    "crypt 1 continue": {
        "text_id": "dialogue.crypt_1_continue",
        "next": "crypt 1 continue check",
    },


    # see if dialogue should mention disturbing the ritual or not
    "crypt 1 continue check": {
        "text_id": "dialogue.crypt_1_continue_check",
        "actions": [
            {   
                "type": "check_flag",
                "target": "crypt_1_empty",
                "value": True,
                "if_pass": "crypt 1 continue choice",
                "if_fail": "crypt 1 reconsider 1",
            }
        ]
    },


    "crypt 1 reconsider 1": {
        "text_id": "dialogue.crypt_1_reconsider_1",
        "next": "crypt 1 reconsider 2"
    },

    "crypt 1 reconsider 2": {
        "text_id": "dialogue.crypt_1_reconsider_2",
        "next": "crypt 1 continue choice"
    },


    "crypt 1 continue choice": {
        "text_id": "dialogue.crypt_1_continue_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.crypt_1_continue_2",
                "next": "enter crypt 2"
            },
            2: {
                "text_id": "dialogue.option.empty",
                "next": "crypt 1 continue choice"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "crypt 1 continue choice"
            },
            4: {
                "text_id": "dialogue.option.crypt_1_step_away",
                "next": "crypt 1 choice"
            }
        }
    },



    "enter crypt 2": {
        "text_id": "dialogue.enter_crypt_2",
        "next": "crypt 2 intro",
        "actions": [
            {   
                "type": "map",
                "target": "crypt 2"
            }
        ]
    },


    "crypt 2 intro": {
        "text_id": "dialogue.crypt_2_intro",
        "next": "crypt 2 main check"
    },

    "crypt 2 main check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "crypt_2_empty",
                "value": True,
                "if_pass": "crypt 2 intro B",
                "if_fail": "crypt 2 intro",
            }
        ]
    },

    "crypt 2 intro B": {
        "text_id": "dialogue.crypt_2_intro_b",
        "next": "crypt 2 choice"
    },

    "crypt 2 cont": {
        "text_id": "dialogue.crypt_2_cont",
        "next": "crypt 2 choice"
    },


    "crypt 2 choice": {
        "text_id": "dialogue.crypt_2_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.crypt_2_explore",
                "next": "crypt 2 explore 1"
            },
            2: {
                "text_id": "dialogue.option.crypt_2_enemies",
                "next": "crypt 2 enemies choice"
            },
            3: {
                "text_id": "dialogue.option.crypt_2_continue",
                "next": "crypt 2 continue"
            },
            4: {
                "text_id": "dialogue.option.crypt_2_return",
                "next": "crypt 1 return"
            }
        }
    },

    "crypt 2 explore 1": {
        "text_id": "dialogue.crypt_2_explore_1",
        "actions": [
            {   
                "type": "check_flag",
                "target": "crypt_2_empty",
                "value": False,
                "if_pass": "crypt 2 explore start",
                "if_fail": "crypt 2 explore empty",
            }
        ]
    },


    "crypt 2 explore start": {
        "text_id": "dialogue.crypt_2_explore_2",
        "next": "crypt 2 choice",
        "actions": [
            {
                "type": "set_flag",
                "target": "crypt_2_empty",
                "value": True
            },
            {   
                "type": "explore_items",
                "target": "crypt_2",
            }
        ]
    },

    "crypt 2 explore empty": {
        "text_id": "dialogue.crypt_2_explore_empty",
        "next": "crypt 2 choice",
    },


    "crypt 2 enemies choice": {
        "text_id": "dialogue.crypt_2_enemies_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.crypt_2_enemies_1",
                "next": "crypt 2 enemies 1"
            },
            2: {
                "text_id": "dialogue.option.crypt_2_enemies_2",
                "next": "crypt 2 enemies 2"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "crypt 2 enemies choice"
            },
            4: {
                "text_id": "dialogue.option.crypt_2_do_nothing",
                "next": "crypt 2 choice"
            }
        }
    },



    # new nodes
    "crypt 2 enemies 1": {
        "text_id": "dialogue.crypt_2_enemies_1",
        "next": "crypt 2 enemies 1 cont",
        "actions": [
            {   
                "type": "encounter",
                "target": "crypt_2_enemies_1",
            }
        ]
    },


    "crypt 2 enemies 1 cont": {
        "text_id": "dialogue.crypt_2_enemies_1_cont",
        "next": "crypt 2 choice",
    },


    "crypt 2 enemies 2": {
        "text_id": "dialogue.crypt_2_enemies_2",
        "next": "crypt 2 enemies 2 cont",
        "actions": [
            {   
                "type": "encounter",
                "target": "crypt_2_enemies_2",
            }
        ]
    },


    "crypt 2 enemies 2 cont": {
        "text_id": "dialogue.crypt_2_enemies_2_cont",
        "next": "crypt 2 choice",
    },


    "crypt 1 return": {
        "text_id": "dialogue.return_to_crypt_1",
        "next": "crypt 1 choice",
        "actions": [
            {   
                "type": "map",
                "target": "crypt 1"
            }
        ]
    },

    "crypt 2 continue": {
        "text_id": "dialogue.crypt_2_continue",
        "next": "crypt 2 continue check",
    },

    # I need to figure out if I want a confirmation or not
    "crypt 2 continue check": {
        "text_id": "dialogue.crypt_2_continue_check",
        "actions": [
            {   
                "type": "check_flag",
                "target": "crypt_2_empty",
                "value": True,
                "if_pass": "crypt 2 continue choice",
                "if_fail": "crypt 2 reconsider 1",
            }
        ]
    },


    "crypt 2 reconsider 1": {
        "text_id": "dialogue.crypt_2_reconsider_1",
        "next": "crypt 2 reconsider 2"
    },

    "crypt 2 reconsider 2": {
        "text_id": "dialogue.crypt_2_reconsider_2",
        "next": "crypt 2 continue choice"
    },


    "crypt 2 continue choice": {
        "text_id": "dialogue.crypt_2_continue_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.crypt_2_continue_2",
                "next": "enter crypt 3"
            },
            2: {
                "text_id": "dialogue.option.empty",
                "next": "crypt 2 continue choice"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "crypt 2 continue choice"
            },
            4: {
                "text_id": "dialogue.option.crypt_2_step_away",
                "next": "crypt 2 choice"
            }
        }
    },



    "enter crypt 3": {
        "text_id": "dialogue.enter_crypt_3",
        "next": "crypt 3 main check",
        "actions": [
            {   
                "type": "map",
                "target": "crypt 3"
            }
        ]
    },

    "crypt 3 main check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "crypt_3_empty",
                "value": True,
                "if_pass": "crypt 3 intro B",
                "if_fail": "crypt 3 intro",
            }
        ]
    },

    "crypt 3 intro B": {
        "text_id": "dialogue.crypt_3_intro_b",
        "next": "crypt 3 choice"
    },

    "crypt 3 intro": {
        "text_id": "dialogue.crypt_3_intro",
        "next": "crypt 3 cont"
    },

    "crypt 3 cont": {
        "text_id": "dialogue.crypt_3_cont",
        "next": "crypt 3 choice"
    },


    "crypt 3 choice": {
        "text_id": "dialogue.crypt_3_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.crypt_3_inspect_items",
                "next": "crypt 3 inspect items"
            },
            2: {
                "text_id": "dialogue.option.crypt_3_inspect_tomb",
                "next": "crypt 3 tomb check"
            },
            3: {
                "text_id": "dialogue.option.crypt_3_approach_people",
                "next": "crypt 3 approach people check"
            },
            4: {
                "text_id": "dialogue.option.crypt_3_return",
                "next": "crypt 2 return"
            }
        }
    },

    # inspect items dialogue
    "crypt 3 inspect items": {
        "text_id": "dialogue.crypt_3_inspect_items",
        "next": "crypt 3 items choice"
    },


    "crypt 3 items choice": {
        "text_id": "dialogue.crypt_3_items_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.crypt_3_inspect_tome",
                "next": "crypt 3 inspect tome"
            },
            2: {
                "text_id": "dialogue.option.crypt_3_inspect_page",
                "next": "crypt 3 inspect page"
            },
            3: {
                "text_id": "dialogue.option.crypt_3_inspect_forbidden",
                "next": "crypt 3 inspect forbidden"
            },
            4: {
                "text_id": "dialogue.option.crypt_3_do_nothing",
                "next": "crypt 3 choice"
            }
        }
    },

    # check if tome was already read.
    # if read -> short version (summary)
    # if not read -> long version
    "crypt 3 inspect tome": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "family_history_known",
                "value": False,
                "if_pass": "crypt 3 tome 2",
                "if_fail": "crypt 3 tome summary",
            }
        ]
    },   

    "crypt 3 tome 2": {
        "text_id": "dialogue.crypt_3_tome_2",
        "next": "crypt 3 tome 3",
    },

    "crypt 3 tome 3": {
        "text_id": "dialogue.crypt_3_tome_3",
        "next": "crypt 3 tome 4",
    },


    "crypt 3 tome 4": {
        "text_id": "dialogue.crypt_3_tome_4",
        "next": "crypt 3 items choice",
        "actions": [
            {
                "type": "set_flag",
                "target": "family_history_known",
                "value": True
            }
        ]
    },

    # add more nodes if needed
    "crypt 3 tome summary": {
        "text_id": "dialogue.crypt_3_tome_summary",
        "next": "crypt 3 items choice",
    },


    # check if note was already read.
    # if read -> short version (summary)
    # if not read -> long version
    "crypt 3 inspect page": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "amulet_known",
                "value": False,
                "if_pass": "crypt 3 page 2",
                "if_fail": "crypt 3 page summary",
            }
        ]
    },   

    "crypt 3 page 2": {
        "text_id": "dialogue.crypt_3_page_2",
        "next": "crypt 3 page 3",
    },

    "crypt 3 page 3": {
        "text_id": "dialogue.crypt_3_page_3",
        "next": "crypt 3 page 4",
    },


    "crypt 3 page 4": {
        "text_id": "dialogue.crypt_3_page_4",
        "next": "crypt 3 items choice",
        "actions": [
            {
                "type": "set_flag",
                "target": "amulet_known",
                "value": True
            }
        ]
    },

    # add more nodes if needed
    "crypt 3 page summary": {
        "text_id": "dialogue.crypt_3_page_summary",
        "next": "crypt 3 items choice",
    },


    # check if note was already read.
    # if read -> short version (summary)
    # if not read -> long version
    "crypt 3 inspect forbidden": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "amulet_known",
                "value": True,
                "if_pass": "crypt 3 forbidden 2",
                "if_fail": "crypt 3 forbidden warning",
            }
        ]
    },   

    # puts on amulet
    "crypt 3 forbidden 2": {
        "text_id": "dialogue.crypt_3_forbidden_2",
        "next": "crypt 3 forbidden 3",
    },

    "crypt 3 forbidden 3": {
        "text_id": "dialogue.crypt_3_forbidden_3",
        "next": "crypt 3 forbidden 4",
    },

    "crypt 3 forbidden 4": {
        "text_id": "dialogue.crypt_3_forbidden_4",
        "next": "crypt 3 forbidden 5",
    },

    "crypt 3 forbidden 5": {
        "text_id": "dialogue.crypt_3_forbidden_5",
        "next": "crypt 3 forbidden 6",
    },

    "crypt 3 forbidden 6": {
        "text_id": "dialogue.crypt_3_forbidden_6",
        "next": "crypt 3 forbidden 7",
    },

    "crypt 3 forbidden 7": {
        "text_id": "dialogue.crypt_3_forbidden_7",
        "next": "crypt 3 items choice",
        "actions": [
            {
                "type": "set_flag",
                "target": "reaper_knowledge",
                "value": True
            }
        ]
    },

    # add more nodes if needed
    "crypt 3 forbidden warning": {
        "text_id": "dialogue.crypt_3_forbidden_warning",
        "next": "crypt 3 forbidden choice",
    },

    "crypt 3 forbidden choice": {
        "text_id": "dialogue.crypt_3_forbidden_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.crypt_3_forbidden_read",
                "next": "forbidden open"
            },
            2: {
                "text_id": "dialogue.option.crypt_3_forbidden_dont_read",
                "next": "crypt 3 items choice"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "crypt 3 forbidden choice"
            },
            4: {
                "text_id": "dialogue.option.empty",
                "next": "crypt 3 forbidden choice"
            },
        }
    },


    "crypt 3 tomb check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "crypt_3_empty",
                "value": False,
                "if_pass": "crypt 3 inspect tomb 1",
                "if_fail": "crypt 3 tomb empty",
            }
        ]
    },

    "crypt 3 inspect tomb 1": {
        "text_id": "dialogue.crypt_3_tomb_1",
        "next": "crypt 3 inspect tomb 2"
    },

    "crypt 3 inspect tomb 2": {
        "text_id": "dialogue.crypt_3_tomb_2",
        "next": "crypt 3 choice",
        "actions": [
            {
                "type": "set_flag",
                "target": "crypt_3_empty",
                "value": True
            },
            {   
                "type": "item",
                "target": "Shiny Key",
                "value": 1
            }
        ]
    },

    "crypt 3 tomb empty": {
        "text_id": "dialogue.crypt_3_tomb_empty",
        "next": "crypt 3 choice",
    },

    # WIP
    # check if lord resolved: true: empty room, false: check if slain
    "crypt 3 approach people check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "lord_resolved",
                "value": True,
                "if_pass": "crypt 3 paladin chest check",
                "if_fail": "crypt 3 lord defeated check",
            }
        ]
    },

    # check if the player looted the chest or not, I don't want accidentally pressing this option again to bypass the steps to be a paladin
    "crypt 3 paladin chest check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "paladin_chest_looted",
                "value": True,
                "if_pass": "crypt 3 paladin check",
                "if_fail": "crypt 3 empty room",
            }
        ]
    },


    # check if the player is a paladin or not. False -> empty room, True -> altar scene
    "crypt 3 paladin check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_class",
                "target": "Paladin",
                "if_pass": "crypt 3 empty room",
                "if_fail": "crypt 3 altar scene",
            }
        ]
    },

    # empty room node
    "crypt 3 empty room": {
        "text_id": "dialogue.crypt_3_empty_room",
        "next": "crypt 3 choice",
    },

    # altar scene approaching and kneeling
    "crypt 3 altar scene": {
        "text_id": "dialogue.crypt_3_altar_scene",
        "next": "crypt 3 paladin choice",
    },

    # ask if you want to attempt to bind with the amulet to become a paladin 
    "crypt 3 paladin choice": {
        "text_id": "dialogue.crypt_3_paladin_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.crypt_3_paladin_accept",
                "next": "crypt 3 paladin 1"
            },
            2: {
                "text_id": "dialogue.option.crypt_3_paladin_decline",
                "next": "crypt 3 paladin decline"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "crypt 3 paladin choice"
            },
            4: {
                "text_id": "dialogue.option.empty",
                "next": "crypt 3 paladin choice"
            }
        }
    },

    # decline path -> comment on uncertianty -> return to crypt choice 3
    "crypt 3 paladin decline": {
        "text_id": "dialogue.crypt_3_paladin_decline",
        "next": "crypt 3 choice",
    },

    # accept path -> confident
    "crypt 3 paladin 1": {
        "text_id": "dialogue.crypt_3_paladin_1",
        "next": "crypt 3 paladin 2",
    },

    # grabs amulet and closes eyes
    "crypt 3 paladin 2": {
        "text_id": "dialogue.crypt_3_paladin_2",
        "next": "crypt 3 paladin 3",
    },

    # recites the oath
    "crypt 3 paladin 3": {
        "text_id": "dialogue.crypt_3_paladin_3",
        "next": "crypt 3 paladin 4",
    },

    # surrounded by light
    "crypt 3 paladin 4": {
        "text_id": "dialogue.crypt_3_paladin_4",
        "next": "crypt 3 paladin 5",
    },

    # paladin unlocked
    "crypt 3 paladin 5": {
        "text_id": "dialogue.crypt_3_paladin_5",
        "next": "crypt 3 paladin 6",
        "actions": [
            {
                "type": "set_class",
                "target": "Paladin",
                "value": True
            }
        ]
    },

    # now I must save my family
    "crypt 3 paladin 6": {
        "text_id": "dialogue.crypt_3_paladin_6",
        "next": "crypt 3 choice",
    },

    # check if lord is slain: true: room filled with dead bodies, false: check if deal is accepted
    "crypt 3 lord defeated check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "lord_defeated",
                "value": True,
                "if_pass": "crypt 3 bodies",
                "if_fail": "crypt 3 deal check",
            }
        ]
    },

    # dead bodies node
    "crypt 3 bodies": {
        "text_id": "dialogue.crypt_3_bodies",
        "next": "crypt 3 choice",
    },

    # check if deal accepted: true: combat, false: regular conversation
    "crypt 3 deal check": {
        "text_id": "dialogue.empty",
        "actions": [
            {   
                "type": "check_flag",
                "target": "accepted_deal",
                "value": True,
                "if_pass": "crypt 3 combat 1",
                "if_fail": "crypt 3 conversation 1",
            }
        ]
    },

    # regular convo node
    "crypt 3 conversation 1": {
        "text_id": "dialogue.crypt_3_conversation_1",
        "next": "crypt 3 conversation 2",
    },

    "crypt 3 conversation 2": {
        "text_id": "dialogue.crypt_3_conversation_2",
        "next": "crypt 3 conversation 3",
    },

    "crypt 3 conversation 3": {
        "text_id": "dialogue.crypt_3_conversation_3",
        "next": "crypt 3 conversation 4",
    },

    # set resolved to true
    "crypt 3 conversation 4": {
        "text_id": "dialogue.crypt_3_conversation_4",
        "next": "crypt 3 choice",
        "actions": [
            {
                "type": "set_flag",
                "target": "lord_resolved",
                "value": True
            }
        ]
    },

    # conversation leading to combat
    "crypt 3 combat 1": {
        "text_id": "dialogue.crypt_3_combat_1",
        "next": "crypt 3 combat 2",
    },

    "crypt 3 combat 2": {
        "text_id": "dialogue.crypt_3_combat_2",
        "next": "crypt 3 combat 3",
    },

    "crypt 3 combat 3": {
        "text_id": "dialogue.crypt_3_combat_3",
        "next": "crypt 3 lord encounter",
    },

    # encounter
    "crypt 3 lord encounter": {
        "text_id": "dialogue.crypt_3_lord_encounter",
        "next": "crypt 3 combat final",
        "actions": [
            {   
                "type": "encounter",
                "target": "crypt_3_graye_encounter",
            }
        ]
    },


    # set slain to true
    "crypt 3 combat final": {
        "text_id": "dialogue.crypt_3_combat_final",
        "next": "crypt 3 choice",
        "actions": [
            {
                "type": "set_flag",
                "target": "lord_defeated",
                "value": True
            }
        ]
    },



    "crypt 2 return": {
        "text_id": "dialogue.return_to_crypt_2",
        "next": "crypt 2 choice",
        "actions": [
            {   
                "type": "map",
                "target": "crypt 2"
            }
        ]
    },     




    "Not Yet Implemented": {
        "text_id": "dialogue.not_yet_implemented",
        "next": "Not Yet Implemented"
    },

}
