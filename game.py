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
    while True:
        for i in range(numEnemyFish):
            fishes.append(random.randint(1, 9))

        if startFish <= min(fishes):
            fishes.clear()
            continue
        else:
            break
    print("Round", round)
    print("Your fish size:", startFish)
    print("You have the following choices. Choose wisely")
    for i in range(numEnemyFish):
        print(f"Opt{i + 1}: Size {fishes[i]}", end="   ")
    while True:
        choice = int(input("Your choices:"))
        if (choice < numEnemyFish):
            break
        else:
            print("Invalid input (Too big or not a integer)")
            continue
    if fishes[choice - 1] < startFish:
        round += 1
        continueChoice = input("Do you want to continue? YES = 1/NO = 2: ")
        if continueChoice == "1":
            fishes.clear()
            continue
        else:
            print("Exiting...")
            break
    else:
        print("Fish too big to eat. You lose.")
        break

