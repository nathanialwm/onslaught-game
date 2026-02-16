from data.enemy import Enemy
def exponential_weighted_average(enemy, alpha=0.9):
    if enemy.id > 20:
        last_20_enemies = Enemy.get_all()[-20:]
    print(str(enemny) for enemny in last_20_enemies)
    weights = [alpha ** (len(last_20_enemies) - 1 - i) for i in range(len(last_20_enemies))]
    return sum(w * v for w, v in zip(weights, last_20_enemies)) / sum(weights)

exponential_weighted_average(Enemy.get_by_name("Skeleton"))