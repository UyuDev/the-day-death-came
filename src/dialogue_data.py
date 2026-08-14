

DIALOGUE = {
    "intro": {
        "text": "You suddenly wake up and get out of bed.",
        "next": "look around"
    },

    "look around": {
        "text": "What do you want to do?",
        "options": {
            1: {
                "text": "Open the trapdoor",
                "next": "trapdoor"
            },
            2: {
                "text": "Go upstairs",
                "next": "stairs"
            },
            3: {
                "text": "Leave through the door",
                "next": "door"
            },
            4: {
                "text": "Examine the table",
                "next": "table"
            }
        }
    },

    "trapdoor": {
        "text": "You open the trapdoor and climb down...",
        "next": "You died."
    },

    "stairs": {
        "text": "You climb the stairs...",
        "next": "You died."
    },

    "door": {
        "text": "You leave through the door...",
        "next": "You died."
    },

    "You died.": {
        "text": "You died.",
        "next": "intro"
    },

    "table": {
        "text": "There is a wooden table covered in dust.",
        "next": "inspect table"
    },

    "inspect table": {
            "text": "You find a book titled 'Tales of the Past'",
            "next": "flip pages"
        },

    "flip pages": {
                "text": "You open up the book and flip through the pages.",
                "next": "sudden flash"
            },

    "sudden flash": {
                    "text": "There is a sudden flash of light.",
                    "next": "intro"
                },
}