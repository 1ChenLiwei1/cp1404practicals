import random
NUMBER_OF_RANDOM_NUMBERS = 6
quick_picks_number = int(input('How many quick picks? '))
for i in range(quick_picks_number):
    CONSTANTS = []
    for j in range(NUMBER_OF_RANDOM_NUMBERS):
        random_number = random.randint(1, 45)
        if random_number in CONSTANTS:
            random_number = random.randint(1, 45)
        CONSTANTS.append(random_number)
    CONSTANTS.sort()
    max_number = max(len(str(number))for number in CONSTANTS)
    print(" ".join(f"{number:{max_number}}" for number in CONSTANTS))

