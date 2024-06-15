import random


def main():
    score = float(input("Enter score: "))
    result = estimate_score(score)
    print(result)
    random_score = random.randint(0, 100)
    print(random_score)


def estimate_score(score):
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        elif score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"


main()