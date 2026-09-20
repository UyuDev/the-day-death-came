

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
                "text_id": "dialogue.option.leave_door",
                "next": "door"
                
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
                "type": "item",
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
            "next": "bed chest 6"
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
                "type": "save_game"
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



    "door": {
        "text_id": "dialogue.leave_door",
        "next": "door encounter"
    },

    "door encounter": {
        "text_id": "dialogue.door_encounter",
        "actions": [
            {   
                "type": "encounter",
                "target": "door_encounter",
                "on_win": "door victory",
                "on_loss": "door death"
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
        "next": "You died"
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
                "if_pass": "table check inventory",
                "if_fail": "table empty",
            }
        ]
    },

    "table check inventory": {
        "text_id": "dialogue.table",
        "next": "inspect table",
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
                "next": "Not Yet Implemented"
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


    "inspect crates": {
        "text_id": "dialogue.inspect_crates",
        "next": "crates choice"
    },

    "crates choice": {
        "text_id": "dialogue.crates_choice",
        "options": {
            1: {
                "text_id": "dialogue.option.empty",
                "next": "crates choice"
            },
            2: {
                "text_id": "dialogue.option.empty",
                "next": "crates choice"
            },
            3: {
                "text_id": "dialogue.option.empty",
                "next": "crates choice"
            },
            4: {
                "text_id": "dialogue.option.take_nothing",
                "next": "look around the basement"
            }
        }
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
        "actions": [
            {   
                "type": "check_flag",
                "target": "basement_right_wall_checked",
                "value": False,
                "if_pass": "right wall loose bricks",
                "if_fail": "right wall loose bricks",
            }
        ]
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
        "actions": [
            {   
                "type": "check_flag",
                "target": "basement_key_found",
                "value": False,
                "if_pass": "bottom wall loose bricks",
                "if_fail": "done wall",
            }
        ]
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
                "if_pass": "wall use tools R",
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
                "if_pass": "wall use tools S",
                "if_fail": "wall need tools",
            }
        ]
    },

    "wall need tools": {
        "text_id": "dialogue.wall_need_tools",
        "next": "look around the basement"
    },

    "wall use tools S": {
        "text_id": "dialogue.wall_use_tools",
        "next": "basement key found"
    },

    "wall use tools R": {
        "text_id": "dialogue.wall_use_tools",
        "next": "basement door revealed"
    },

    "basement key found": {
        "text_id": "dialogue.basement_key_found",
        "next": "basement key check",
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

    "basement key check": {
        "text_id": "dialogue.basement_key_found",
        "actions": [
            {   
                "type": "check_flag",
                "target": "basement_walls_broken",
                "value": False,
                "if_pass": "look around the basement",
                "if_fail": "look around the basement 2",
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
                "next": "basement door inspect"
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

    "basement door inspect": {
        "text_id": "dialogue.basement_door_inspect",
        "actions": [
            {   
                "type": "check_flag",
                "target": "basement_key_found",
                "value": False,
                "if_pass": "basement door locked",
                "if_fail": "basement door unlock",
            }
        ]
    },

    "basement door locked": {
        "text_id": "dialogue.basement_door_locked",
        "next": "look around the basement 2"
    },

    "basement door unlock": {
        "text_id": "dialogue.basement_door_unlock",
        "next": "enter tunnel check",
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
                "text_id": "dialogue.option.empty",
                "next": "look around the basement 2"
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



    "enter tunnel check": {
        "text_id": "dialogue.enter_tunnel_check",
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
        "next": "tunnel 1 cont"
    },

    "tunnel 1 cont": {
        "text_id": "dialogue.tunnel_1_cont",
        "next": "tunnel 1 encounter"
    },

    "tunnel 1 encounter": {
        "text_id": "dialogue.tunnel_1_encounter",
        "next": "tunnel 1 reaction 1",
        "actions": [
            {   
                "type": "encounter",
                "target": "tunnel_1_encounter"
            }
        ]
    },

    "tunnel 1 reaction 1": {
        "text_id": "dialogue.tunnel_1_reaction_1",
        "next": "tunnel 1 reaction 2"
    },

    "tunnel 1 reaction 2": {
        "text_id": "dialogue.tunnel_1_reaction_2",
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
        "next": "tunnel 2 intro",
        "actions": [
            {   
                "type": "map",
                "target": "tunnel 2"
            }
        ]
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
        "next": "sewer intro",
        "actions": [
            {   
                "type": "map",
                "target": "sewer"
            }
        ]
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
        "next": "dungeon intro",
        "actions": [
            {   
                "type": "map",
                "target": "dungeon"
            }
        ]
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
                "target": "crypt_door_unlocked",
                "value": True,
                "if_pass": "enter crypt 1",
                "if_fail": "dungeon crypt key check",
            }
        ]
    },

    "dungeon crypt key check": {
        "text_id": "dialogue.dungeon_continue_check",
        "actions": [
            {   
                "type": "check_flag",
                "target": "dungeon_empty",
                "value": True,
                "if_pass": "dungeon unlock crypt",
                "if_fail": "dungeon crypt locked 1",
            }
        ]
    },

    "dungeon crypt locked 1": {
        "text_id": "dialogue.dungeon_crypt_locked_1",
        "next": "dungeon crypt locked 2"
    },

    "dungeon crypt locked 2": {
        "text_id": "dialogue.dungeon_crypt_locked_2",
        "next": "dungeon choice"
    },

    "dungeon unlock crypt": {
        "text_id": "dialogue.dungeon_unlock_crypt",
        "next": "enter crypt 1",
        "actions": [
            {   
                "type": "set_flag",
                "target": "crypt_door_unlocked",
                "value": True
            }
        ]
    },

    "enter crypt 1": {
        "text_id": "dialogue.enter_crypt_1",
        "next": "crypt 1 intro",
        "actions": [
            {   
                "type": "map",
                "target": "crypt 1"
            }
        ]
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
                "next": "dungeon return"
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
                "if_fail": "crypt 1 explore empty",
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

    "crypt 1 explore empty": {
        "text_id": "dialogue.crypt_1_explore_empty",
        "next": "crypt 1 choice",
    },

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



    # new nodes
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


    "dungeon return": {
        "text_id": "dialogue.return_to_dungeon",
        "next": "dungeon choice",
        "actions": [
            {   
                "type": "map",
                "target": "dungeon"
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
        "next": "crypt 2 cont"
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
        "next": "crypt 3 intro",
        "actions": [
            {   
                "type": "map",
                "target": "crypt 3"
            }
        ]
    },


    "Not Yet Implemented": {
        "text_id": "dialogue.not_yet_implemented",
        "next": "Not Yet Implemented"
    },

}
