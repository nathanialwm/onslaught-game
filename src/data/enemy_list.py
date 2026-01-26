from enemy import Enemy

class EnemyList:
    
    def generate_enemies():
        enemy_data = [
            ("Mouse", 10, 2),
            ("Rat", 15, 3),
            ("Bat", 20, 4),
            ("Spider", 25, 5),
            ("Snake", 30, 6),
            ("Goblin", 40, 8)
        ]
        return [Enemy(name, health, attack_power) for name, health, attack_power in enemy_data]