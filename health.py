import random

player_health = 50

difficulty = 3

health_potion = int(random.randint(25, 50) / difficulty)

player_health = player_health + health_potion
print(player_health)