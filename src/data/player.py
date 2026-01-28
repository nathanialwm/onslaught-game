from data.constants import Images

class Player:
    def __init__(self, name, health=100, attack=10, attack_speed=1.5, defense=5,
                position=(0, 0), portrait=Images.PLAYER_PORTRAIT):
        self.name = name
        #initialize battle stats
        self.health = health
        self.attack = attack
        self.attack_speed = attack_speed
        self.defense = defense
        self.temp_health = health
        #initalize animation variables
        self.position = position
        #misc
        self.portrait = portrait

    def take_damage(self, amount):
        self.temp_health -= amount
        if self.temp_health < 0:
            self.temp_health = 0

    def is_alive(self):
        return self.temp_health > 0