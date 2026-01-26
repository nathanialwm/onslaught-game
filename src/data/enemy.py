class Enemy:
    # Class-level registry of all enemies
    _registry = None

    def __init__(self, name, health, attack_power, portrait):
        self.name = name
        self.health = health
        self.temp_health = health
        self.attack_power = attack_power
        self.portrait = portrait

    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"Enemy: {self.name}, Health: {self.health}, Attack Power: {self.attack_power}"

    @classmethod
    def _init_registry(cls):
        if cls._registry is None:
            enemy_data = [
                ("Mouse", 10, 2, "../assets/images/mouse.png"),
                ("Rat", 15, 3, "../assets/images/placeholder.png"),
                ("Bat", 20, 4, "../assets/images/placeholder.png"),
                ("Spider", 25, 5, "../assets/images/placeholder.png"),
                ("Snake", 30, 6, "../assets/images/placeholder.png"),
                ("Goblin", 40, 8, "../assets/images/goblin.png")
            ]
            cls._registry = {
                name: cls(name, health, attack, portrait)
                for name, health, attack, portrait in enemy_data
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