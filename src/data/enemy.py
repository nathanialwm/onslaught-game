from data.constants import Images
class Enemy:
    # Class-level registry of all enemies
    _registry = None

    def __init__(self, name, health, attack, defense, portrait):
        self.name = name
        self.health = health
        self.temp_health = health
        self.attack = attack
        self.defense = defense
        self.portrait = portrait

    def attack(self, target):
        target.health -= self.attack
        print(f"{self.name} attacks {target.name} for {self.attack} damage!")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"Enemy: {self.name}, Health: {self.health}, Attack Power: {self.attack}"

    @classmethod
    def _init_registry(cls):
        if cls._registry is None:
            enemy_data = [
                ("Mouse", 10, 2, 3, Images.MOUSE_PORTRAIT),
                ("Rat", 15, 3, 4, Images.PLAYER_PORTRAIT),
                ("Bat", 20, 4, 5, Images.PLAYER_PORTRAIT),
                ("Spider", 25, 5, 6, Images.PLAYER_PORTRAIT),
                ("Snake", 30, 6, 7, Images.PLAYER_PORTRAIT),
                ("Goblin", 40, 8, 8, Images.GOBLIN_PORTRAIT)
            ]
            cls._registry = {
                name: cls(name, health, attack, defense, portrait)
                for name, health, attack, defense, portrait in enemy_data
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