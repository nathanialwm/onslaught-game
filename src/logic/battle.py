import pygame

class Battle:
    def __init__(self, player, enemy, battle_widget):
        self.player = player
        self.enemy = enemy
        self.battle_widget = battle_widget

    def battle_sequence(self):
        # Every new battle - fight until someone is dead
        if self.player.temp_health > 0 and self.enemy.temp_health == 0:
            self.player.exp += self.enemy.exp_reward
            self.player.gold += self.enemy.gold_reward
            self.player.temp_health = self.player.health
            self.enemy.temp_health = self.enemy.health
            self.battle_widget.battle_summary = [
                "",
                f"You defeated {self.enemy.name}!",
                f"Gained {self.enemy.exp_reward} EXP and {self.enemy.gold_reward} Gold."
            ]
            return
        elif self.enemy.temp_health > 0 and self.player.temp_health == 0:
            self.player.temp_health = self.player.health
            self.enemy.temp_health = self.enemy.health
            return
        

    def player_attack(self, PLAYER_ATTACK):
        pygame.time.set_timer(PLAYER_ATTACK, int(self.player.attack_speed * 1000))
        self.enemy.take_damage(self.player.attack)

    def enemy_attack(self, ENEMY_ATTACK):
        pygame.time.set_timer(ENEMY_ATTACK, int(self.enemy.attack_speed * 1000))
        self.player.take_damage(self.enemy.attack)


    