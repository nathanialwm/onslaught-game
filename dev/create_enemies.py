"""
This file will contain a script to use a gui/cli tool to rapidly add enemies to the json data file
"""

import json
user_in = ""
all_enemies = []
def single_enemy():
    enemy_data = {
            "name": "Mouse",
            "level": 1,
            "health": 0,
            "attack": 0,
            "attack_speed": 0.0,
            "defense": 0,
            "accuracy": 0,
            "dodge": 0,
            "exp_reward": 1,
            "gold_reward": 1,
            "rarity_modifier": 1.0
        }
    for key, value in enemy_data.items():
        user_in = input(f"{key}: ")
        if isinstance(value, int):
            enemy_data[key] = int(user_in)
        elif isinstance(value, float):
            enemy_data[key] = float(user_in)
        else:
            enemy_data[key] = user_in
    
    user_in = input("continue? ")
    all_enemies.append(enemy_data)
    return user_in

while user_in != "!":
    user_in = single_enemy()

with open("./src/data/enemies.json", "r+", encoding="utf-8") as f:
    data = json.load(f)
    for enemy in all_enemies:
        data["enemies_list"].append(enemy)
    f.seek(0)
    json.dump(data, f, indent=4)