from data.constants import Images

class Player:
    def __init__(self, name, level=1, health=15, attack=2, attack_speed=2, defense=0,
                accuracy=10, dodge=10, exp=0, gold=0, items=[], position=(0, 0), portrait=Images.PLAYER_PORTRAIT):
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
        #initialize progression stats
        self.exp = exp
        self.gold = gold
        self.items = items
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