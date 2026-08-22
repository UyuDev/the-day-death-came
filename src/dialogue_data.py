

DIALOGUE = {
    "intro": {
        "text_id": "dialogue.intro",
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
        "next": "trapdoor fail"
    },

    "trapdoor fail": {
        "text_id": "dialogue.trapdoor_fail",
        "next": "You died"
    },

    "stairs upward": {
        "text_id": "dialogue.stairs_to_upstairs",
        "next": "upstairs",
        "map": "house_upstairs"
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
                "next": "intro"
            },

    "stairs downward": {
        "text_id": "dialogue.stairs_downward",
        "next": "look around downstairs",
        "map": "house"
    },

    "left bookshelf": {
        "text_id": "dialogue.left_bookshelf",
        "next": "flip pages dark"
    },

    "flip pages dark": {
        "text_id": "dialogue.dark_incant_flip",
        "next": "close pages dark"
    },

    "close pages dark": {
        "text_id": "dialogue.dark_incant_close",
        "next": "look around upstairs"
    },

    "right bookshelf": {
        "text_id": "dialogue.right_bookshelf",
        "next": "reaction forbidden"
    },

    "reaction forbidden": {
        "text_id": "dialogue.forbidden_react",
        "next": "open book forbidden"
    },

    "open book forbidden": {
        "text_id": "dialogue.forbidden_open",
        "next": "foreword forbidden"
    },

    "foreword forbidden": {
        "text_id": "dialogue.forbidden_foreword",
        "next": "bad reaction forbidden"
    },

    "bad reaction forbidden": {
        "text_id": "dialogue.forbidden_bad_react",
        "next": "You collapse on the floor"
    },

    "door": {
        "text_id": "dialogue.leave_door",
        "next": "You collapse on the floor"
    },

    "You collapse on the floor": {
        "text_id": "dialogue.collapse_floor",
        "next": "You died"
    },

    "You died": {
        "text_id": "dialogue.died",
        "next": "intro",
        "map": "house_upstairs"
    },

    "table": {
        "text_id": "dialogue.table",
        "next": "inspect table"
    },

    "inspect table": {
        "text_id": "dialogue.inspect_table",
        "next": "flip pages tales"
    },

    "flip pages tales": {
        "text_id": "dialogue.flip_pages_tales",
        "next": "sudden flash"
    },

    "sudden flash": {
        "text_id": "dialogue.sudden_flash",
        "next": "intro",
        "map": "house_upstairs"
    },
}