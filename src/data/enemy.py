from data.constants import Images
class Enemy:
    # Class-level registry of all enemies
    _registry = None

    def __init__(self, name, health, attack, attack_speed, defense, position, portrait):
        self.name = name
        #initialize battle stats
        self.health = health
        self.temp_health = health
        self.attack = attack
        self.attack_speed = attack_speed
        self.defense = defense
        # animation variables
        self.position = position

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
            enemy_data = [
                ("Mouse", 10, 2, 2, 3, (0,0), Images.MOUSE_PORTRAIT),
                ("Rat", 15, 3, 2, 4, (0,0), Images.PLAYER_PORTRAIT),
                ("Bat", 20, 4, 1.6, 5, (0,0), Images.PLAYER_PORTRAIT),
                ("Spider", 25, 5, 1.2, 6, (0,0), Images.PLAYER_PORTRAIT),
                ("Snake", 30, 6, 1.6, 7, (0,0), Images.PLAYER_PORTRAIT),
                ("Goblin", 40, 8, 1.9, 8, (0,0), Images.GOBLIN_PORTRAIT)
            ]
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