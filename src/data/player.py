class Player:
    def __init__(self, name, health=100, position=(0, 0)):
        self.name = name
        self.health = health
        self.temp_health = health

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0