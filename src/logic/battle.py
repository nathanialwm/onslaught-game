import pygame

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.battle_widget = None

    def battle_sequence(self):
        # Every new battle - fight until someone is dead
        if self.player.temp_health > 0 and self.enemy.temp_health == 0:
            print("winner")

    def player_attack(self, PLAYER_ATTACK):
        pygame.time.set_timer(PLAYER_ATTACK, int(self.player.attack_speed * 1000))
        self.enemy.take_damage(self.player.attack)

    def enemy_attack(self, ENEMY_ATTACK):
        pygame.time.set_timer(ENEMY_ATTACK, int(self.enemy.attack_speed * 1000))
        self.player.take_damage(self.enemy.attack)


    