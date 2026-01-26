# Onslaught

WIP remake of AutoBattle RPG. An incremental mostly text-based autobattling RPG. Fight 100s of monsters, collect unique equipment, build your character to get infinitely stronger!

## Table of Contents

- [Status](#status)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Status

Work in progress.

## Installation

Ensure you have Python 3.x installed.

Clone the repository:
```bash
git clone <your-repo-url>
cd onslaught-game
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the game from the `src` directory:
```bash
cd src
python main.py
```

### Controls

- **Dropdown**: Click to open, scroll or drag to navigate, click to select an enemy
- **ESC**: Close dropdown
- **X**: Close window

## Project Structure

```
onslaught-game/
├── assets/
│   ├── fonts/          # Game fonts
│   └── images/         # Sprites and portraits
├── src/
│   ├── main.py         # Entry point, game loop
│   ├── draw.py         # Rendering and UI drawing
│   ├── data/
│   │   ├── constants.py    # Colors, fonts, game constants
│   │   ├── enemy.py        # Enemy class and registry
│   │   └── player.py       # Player class
│   ├── widgets/
│   │   ├── dropdown.py     # Custom scrollable dropdown
│   │   └── health_bar.py   # Health bar widget
│   └── logic/
│       └── battle.py       # Battle system (WIP)
├── requirements.txt
└── README.md
```
