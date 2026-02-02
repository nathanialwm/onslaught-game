from data.constants import Images
import json
class Enemy:
    # Class-level registry of all enemies
    _registry = None

    def __init__(self, name, health, attack, attack_speed, defense, portrait):
        self.name = name
        #initialize battle stats
        self.health = health
        self.temp_health = health
        self.attack = attack
        self.attack_speed = attack_speed
        self.defense = defense
        # animation variables
        self.position = (0,0)

        self.portrait = portrait

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
            with open("enemies.json", "r", encoding="utf-8") as f:
                loaded_data = json.load(f)
            enemy_data = loaded_data["enemies_list"]
            cls._registry = {
                name: cls(name, health, attack, attack_speed, defense, position, portrait)
                for name, health, attack, attack_speed, defense, position, portrait in enemy_data
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