import json

def load_settings():
    with open("config.json", "r") as file:
        return json.load(file)

def save_settings(settings):
    with open("config.json", "w") as file:
        json.dump(settings, file)

def edit_settings(settings, choice):
    if choice == 1:
        if settings["language"] == "en":
            settings["language"] = "ko"
        elif settings["language"] == "ko":
            settings["language"] = "en"
    elif choice == 2:
        if settings["hardcore"] == True:
            settings["hardcore"] = False
        elif settings["hardcore"] == False:
            settings["hardcore"] = True
    return settings

def load_language(language):
    if language == "en":
        with open("en.json", "r") as file:
            return json.load(file)
    if language == "ko":
        with open("ko.json", "r") as file:
            return json.load(file)