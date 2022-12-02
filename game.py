import random

print("""
Game rule:
You have a fish with a certain value (from 2 to 9)
You have a random set of choices
""")

exit = False
round = 1
fishes = []
while not exit:
    startFish = random.randint(2, 9)
    choice = 0
    numEnemyFish = random.randint(3, 9)
    for i in range(numEnemyFish):
        fishes.append(random.randint(1, 9))

    if startFish <= min(fishes):
        fishes.clear()
        continue
