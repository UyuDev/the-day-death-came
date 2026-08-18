

DIALOGUE = {
    "intro": {
        "text": "You suddenly wake up and get out of bed.",
        "next": "look around upstairs"
    },

    "look around downstairs": {
        "text": "What do you want to do?",
        "options": {
            1: {
                "text": "Open the trapdoor",
                "next": "trapdoor"
            },
            2: {
                "text": "Go upstairs",
                "next": "stairs upward"
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
        "next": "trapdoor fail"
    },

    "trapdoor fail": {
        "text": "Upon reaching the ground you feel intense pain as a bright light surrounds you.",
        "next": "You died"
    },

    "stairs upward": {
        "text": "You walk up the stairs...",
        "next": "upstairs",
        "map": "house_upstairs"
    },

    "upstairs": {
        "text": "You are back upstairs",
        "next": "look around upstairs"
    },

    "look around upstairs": {
        "text": "What do you want to do?",
        "options": {
            1: {
                "text": "Go to the bed",
                "next": "bed"
            },
            2: {
                "text": "Go downstairs",
                "next": "stairs downward"
            },
            3: {
                "text": "Inspect the left bookshelf",
                "next": "left bookshelf"
            },
            4: {
                "text": "Inspect the right bookshelf",
                "next": "right bookshelf"
                }
            }
        },

    "bed": {
            "text": "You get in bed and fall asleep.",
            "next": "sleep"
        },

    "sleep": {
                "text": "Your dream gets interrupted by a strange sensation.",
                "next": "intro"
            },

    "stairs downward": {
        "text": "You go down the stairs...",
        "next": "look around downstairs",
        "map": "house"
    },

    "left bookshelf": {
        "text": "You find a book titled 'A Dark Descent'.",
        "next": "flip pages dark"
    },

    "flip pages dark": {
        "text": "You find a passage labeled 'opening incantation'.",
        "next": "close pages dark"
    },

    "close pages dark": {
        "text": "You close the book and step away.",
        "next": "look around upstairs"
    },

    "right bookshelf": {
        "text": "You find a book titled 'Forbidden Knowledge'.",
        "next": "reaction forbidden"
    },

    "reaction forbidden": {
        "text": "How exciting! I wonder what secrets this contains...",
        "next": "open book forbidden"
    },

    "open book forbidden": {
        "text": "You open the book and read the foreword.",
        "next": "foreword forbidden"
    },

    "foreword forbidden": {
        "text": "In red letters it is written: He who readeth this booke shall die.",
        "next": "bad reaction forbidden"
    },

    "bad reaction forbidden": {
        "text": "I don't feel so good.",
        "next": "You collapse on the floor"
    },

    "door": {
        "text": "You leave through the door...",
        "next": "You collapse on the floor"
    },

    "You collapse on the floor": {
        "text": "You collapse on the floor and the room goes dark.",
        "next": "You died"
    },

    "You died": {
        "text": "You died.",
        "next": "intro"
    },

    "table": {
        "text": "There is a wooden table covered in dust.",
        "next": "inspect table"
    },

    "inspect table": {
        "text": "You find a book titled 'Tales of the Past'",
        "next": "flip pages tales"
    },

    "flip pages tales": {
        "text": "You open up the book and flip through the pages.",
        "next": "sudden flash"
    },

    "sudden flash": {
        "text": "There is a sudden flash of light.",
        "next": "intro"
    },
}