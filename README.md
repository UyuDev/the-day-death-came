# fantasy-rpg

A text-heavy fantasy RPG built in Python with Pygame. Explore a hand-drawn world, fight enemies, make story choices, develop Nicholas into different classes, and uncover the cause of an attack on his home. The game features branching dialogue, multiple endings, save files, character progression, two visual styles, and English/Korean localization.

## Installation

### V1 Release - recommended 

The easiest way to play the game is through the packaged release.

1. Download the latest V1 release from the Releases page.
2. Extract the downloaded folder to your desired location.
3. Run the executable to start the game.
4. See the Controls section below for information on how to play.

### Running from Source

Running from source is primarily intended for developers or anyone interested in viewing or modifying the code.

Requirements

Python 3.13

uv

Clone the repository and enter the project directory:

git clone <repository-url>
cd fantasy-rpg

Install the project's dependencies:

uv sync

Run the game:

./main.sh

The project was developed and tested using WSL/Linux. Running directly on Windows may require launching the Python entry point manually rather than using main.sh.


## Main menu

Refer to the explanation below to understand how to navigate the menu.



### Controls

- **Space / Enter:** Advance dialogue
- **1–4:** Select dialogue or menu options
- **B:** Print the player's full inventory to the terminal. This is intended for players running the game from source and may not display anything when using the packaged executable.
- **C:** Print the player's currently equipped items to the terminal. This is intended for players running the game from source and may not display anything when using the packaged executable.

### Save Slots

The game supports four save slots. The currently selected slot is used both when loading a game and when starting a new game.

Save slot 1 is selected by default. To start a new game in a different slot, first open the Save Slots menu and select the slot you want to use. Starting a new game without changing the selected slot may overwrite progress in the previously selected slot.

To continue an existing game, open the Save Slots menu and select the save you want to load.

Progress is saved by sleeping in a bed. Saving overwrites the data in the currently selected save slot.


### Settings

This game supports text localization and has two separate art styles.

#### Localization:

Currently this game supports English and Korean. 

Developer's note:
I wrote the English and had it reviewed by AI.
The Korean was machine translated and each line was reviewed by me.

### Art Style:

The two options are Tiles and Illustrations. 

Tiles: hand drawn pixel art tiles overlayed onto a grid. Each map was handcrafted by myself and iterated over.
Illustrations: hand drawn art matching the style of the combat illustrations.

Regardless of the choice, the game does include illustrations for key moments.


## Developer's notes

### Summary

I initially wanted to build a text-based RPG to be able to play as one of my OCs in their world. 
The scope quickly grew as I decided to make it not just a programming project, but an art, writing, and localization project as well.

### Worldbuilding

The fantasy world was created years ago, combining the observations and stories I collected over my years gaming since 7 years old.
If you wish to learn more about the lore and other stories of my world, watch this space. I may add a link to more information.

### Story

Despite wanting to play as one of my OCs, I ended up making a new character for this story. For more details read the "How I built this" section.

### How I built this

I wanted to design and implement the game's systems myself rather than have AI generate solutions for me. When I encountered unfamiliar problems, I generally designed an approach first and used AI as a reviewer and debugging aid. If an approach was viable, I deliberately continued with my own design rather than replacing it with an AI-generated implementation.

Naturally, I had some issues as I have 0 experience with main menus, save systems or gamdev in general. I started off attempting to design a system and then I would get AI to check if it would be usable or not. If it was unusable, I would stop there and figure out how to make it work. If it was viable, I stuck to it and avoided having AI give me the best solution. Due to this choice, I had to later go back and redesign a lot of systems to enable their proper interaction.

I started off building a small demo using a house to test interaction with objects and to see if I could get a dialogue system to work. I eventually added more objects, but I needed a way to prevent dead ends and to test death mechanics, so I made almost all choices result in death. I kept this up and treated death and resurrection as part of the story progresison. As I added more features I realized I never even decided on what OC was going to be my protagonist. I eventually decided on making a new character and using a simple backstory: a farmer's son. As I continued desigining the game I found a solid place in my world's lore for this character and was able to write the first draft of the story's plot. 

#### Warning: Spoilers below: skip to the next section if desired.

The Town section was added late into production. I originally had the player transition from the dungeon to the crypts, but it felt really forced. As I designed the town, the proximity to the reaper boss made me want to add more features to support an RTS-style boss farming gameplay, so I added the merchants and inn. I then in one of the final passes added the Blademaster character and fleshed out the main story and Nicholas' goals.

#### End of spoilers

Over a month in as I had to do a lot of writing, I found myself with almost a hundred lines as a time I needed to create dialogue nodes for. I realized then that I should have made a node generator that automates the node creation, naming, localization key generation and actions. With bugtesting I quickly learned that I also should have made a file validator to see that all my dialogue had no dead ends or unused flags. As this is my first time experimenting with gamedev I am not surprised that I had such huge oversights. I take this experience as a huge lesson for future projects.

