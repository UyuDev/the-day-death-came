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
        else:
            settings["language"] = "en"
    elif choice == 2:
        if settings["hardcore"] == True:
            settings["hardcore"] = False
        else:
            settings["hardcore"] = True
    elif choice == 3:
        pass # Disabled for V1
        # if settings["art"] == "tiles":
        #     settings["art"] = "illustrations"
        # else:
        #     settings["art"] = "tiles"
    return settings

def load_language(language):
    with open(f"localization/{language}.json", "r") as file:
        return json.load(file)
