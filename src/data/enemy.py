import logging
import os
from data.constants import Images
import json

logger = logging.getLogger("onslaught_logs")
class Enemy:
    # Class-level registry of all enemies
    _registry = None

    def __init__(self, name, level, health, attack, attack_speed, defense, accuracy, dodge, exp_reward, gold_reward, rarity_modifier):
        self.name = name
        self.level = level
        #initialize battle stats
        self.health = health
        self.temp_health = health
        self.attack = attack
        self.attack_speed = attack_speed
        self.defense = defense
        self.accuracy = accuracy
        self.dodge = dodge
        #reward stats
        self.exp_reward = exp_reward
        self.gold_reward = gold_reward
        self.rarity_modifier = rarity_modifier
        # animation variables
        self.position = (0,0)
        #Set portrait path based on name
        self.portrait = os.path.join(
            os.path.dirname(__file__), "..", "..", "assets", "images", f"{self.name.lower()}.png")

    def take_damage(self, amount):
        self.temp_health -= amount
        if self.temp_health < 0:
            self.temp_health = 0

    def is_alive(self):
        return self.temp_health > 0

    def __str__(self):
        return f"Enemy: {self.name}, Health: {self.health}, Attack Power: {self.attack}"

    @classmethod
    def _init_registry(cls):
        if cls._registry is None:
            """
            Name, heatlth, attack, attack_speed, defense, position, portrait
            """
            with open("./src/data/enemies.json", "r", encoding="utf-8") as f:
                loaded_data = json.load(f)
            enemy_data = loaded_data["enemies_list"]
            cls._registry = {
                enemy_dict["name"]: Enemy(
                    name=enemy_dict["name"],
                    level=enemy_dict["level"],
                    health=enemy_dict["health"],
                    attack=enemy_dict["attack"],
                    attack_speed=enemy_dict["attack_speed"],
                    defense=enemy_dict["defense"],
                    accuracy=enemy_dict["accuracy"],
                    dodge=enemy_dict["dodge"],
                    exp_reward=enemy_dict["exp_reward"],
                    gold_reward=enemy_dict["gold_reward"],
                    rarity_modifier=enemy_dict["rarity_modifier"]
                )
                for enemy_dict in enemy_data
            }

    @classmethod
    def get_all(cls):
        """Returns list of all Enemy objects"""
        cls._init_registry()
        return list(cls._registry.values())

    @classmethod
    def get_by_name(cls, name):
        """Returns Enemy object by name, or None if not found"""
        cls._init_registry()
        return cls._registry.get(name)