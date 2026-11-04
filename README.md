# The Day Death Came

A text-heavy fantasy RPG built in Python with Pygame. Explore a handcrafted pixel-art world, fight enemies, make story choices, develop Nicholas into different classes, collect and upgrade equipment, and uncover the cause of an attack on his home.

The game features branching dialogue, multiple endings, save files, character progression, inventory and equipment management, and English/Korean localization.

## Installation

### V1 Release — Windows Only

The easiest way to play the game is through the packaged Windows release.

1. Download the latest V1 release from the [Releases](https://github.com/UyuDev/the-day-death-came/releases) page.
2. Extract the downloaded ZIP file to your desired location.
3. Run `TheDayDeathCame.exe` to start the game.
4. See the Controls section below for information on how to play.

### Running from Source

Running from source is primarily intended for developers or anyone interested in viewing or modifying the code.

**Requirements**
- Python 3.13
- [uv](https://docs.astral.sh/uv/)

Clone the repository and enter the project directory:

```bash
git clone https://github.com/UyuDev/the-day-death-came
cd the-day-death-came
```

Install the project's dependencies:

```bash
uv sync
```

Run the game:

```bash
./main.sh
```

The project was developed primarily using WSL/Linux. The V1 packaged release was tested on Windows. Running directly from source on Windows may require launching the Python entry point manually rather than using `main.sh`.


## Main menu

Refer to the explanation below to understand how to navigate the menu.



### Controls

- **Space / Enter:** Advance dialogue
- **1–4:** Select dialogue or menu options
- **B/C:** Open the in-game inventory interface to view and browse collected items or currently equipped gear.


### Inventory and Equipment

The game features an inventory and equipment system with dedicated in-game interfaces for browsing collected items and inspecting equipped gear.

Items are collected automatically during exploration and combat. When acquiring equipment, the game compares its power against the player's currently equipped gear and automatically equips upgrades. Replaced equipment is returned to the inventory.

Inventory space is limited, but larger bags increase carrying capacity. Quest-related key items are stored separately on a keyring and do not occupy regular inventory slots.

The inventory interface displays collected items and available space, while the equipment interface shows currently equipped gear and its power.

Inventory contents, equipment, carrying capacity, and key items are preserved when saving and loading the game.

### Save Slots

The game supports four save slots. The currently selected slot is used both when loading a game and when starting a new game.

Save slot 1 is selected by default. To start a new game in a different slot, first open the Save Slots menu and select the slot you want to use. Starting a new game without changing the selected slot may overwrite progress in the previously selected slot.

To continue an existing game, open the Save Slots menu and select the save you want to load.

Progress is saved by sleeping in a bed. Saving overwrites the data in the currently selected save slot.


### Settings

This game supports text localization and has an optional Hardcore mode.

#### Localization:

Currently this game supports English and Korean. 

Developer's note:
The English dialogue was written by me and reviewed with AI assistance. The Korean localization was initially machine-translated, then reviewed line by line by me.


### Game Difficulty:

Normal Mode: Death returns you to your last saved checkpoint. Progress made since saving is lost.

Hardcore Mode: Death resets your character and world progress, replacing your current save with a fresh game.


### Art Style

The game uses handcrafted pixel-art tiles displayed on a grid. Each environment was designed and iterated on individually, including the buildings, terrain, and environmental details.

The game also features hand-drawn artwork for the main menu, enemies and lootable containers.


## Developer's Notes

### Summary

I initially wanted to build a text-based RPG so I could play as one of my original characters (OCs) in their world.

The scope quickly grew as I decided to make it not just a programming project, but an art, writing, and localization project as well.

### Worldbuilding

I began creating this fantasy world years ago, drawing on the stories, ideas, and observations I collected through my experiences with games over the years.

If you wish to learn more about the lore and other stories set in my world, watch this space. I may add a link to more information in the future.

### Story

Despite originally wanting to play as one of my OCs, I ended up creating a new character for this story. For more details, read the "How I Built This" section.

### How I Built This

I wanted to design and implement the game's systems myself rather than have AI generate solutions for me. When I encountered unfamiliar problems, I generally designed an approach first and used AI as a reviewer and debugging aid. If an approach was viable, I deliberately continued with my own design rather than replacing it with an AI-generated implementation.

Naturally, I ran into problems because I had no prior experience implementing main menus, save systems, or game development systems in general. I would first attempt to design a system and then ask AI to evaluate whether my approach was workable. If it wasn't, I would reconsider the design and figure out how to make it work. If it was viable, I stuck with it rather than asking for the optimal solution. As a result, I eventually had to go back and redesign several systems to allow them to interact properly.

I started by building a small demo set inside a house to test interactions with objects and see whether I could get a dialogue system working. I eventually added more objects, but I needed a way to prevent dead ends and test the death mechanics, so I made almost every choice result in death. I continued with this approach, treating death and resurrection as part of the story's progression.

As I added more features, I realized I hadn't even decided which OC would be the protagonist. I eventually chose to create a new character with a simple backstory: a farmer's son. As I continued designing the game, I found a suitable place for this character in my world's lore and was able to write the first draft of the story's plot.

#### Warning: Spoilers below. Skip to the next section if desired.

The town section was added late in development. Originally, the player transitioned directly from the dungeon to the crypts, but this felt forced. As I designed the town, its proximity to the Reaper boss inspired me to introduce a repeatable boss-farming loop, so I added merchants and an inn to support character progression between encounters. During one of the final development passes, I also introduced the character who would eventually become Galerich and fleshed out the main story and Nicholas's goals.

#### End of spoilers

More than a month into development, I found myself writing almost a hundred lines of dialogue at a time, all of which needed corresponding dialogue nodes. I realized that I should have created a node generator to automate node creation, naming, localization key generation, and actions.

During bug testing, I also realized that I should have built a validator to identify dead ends, missing dialogue references, and unused flags.

Since this was my first experience with game development, I'm not surprised that I made such significant oversights. I've taken these experiences as valuable lessons for future projects.

