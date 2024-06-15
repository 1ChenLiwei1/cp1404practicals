MENU = "(G)\n(P)\n(S)\n(Q)"


def main():
    print(MENU)
    choice = get_choice()
    while choice != "Q":
        if choice == "G":
            score = get_score()
            print(score)
        elif choice == "p":
            score = get_score()
            result = estimate_score(score)
            print(result)
        else:
            score = get_score()
            show_stars(score)
        choice = get_choice()
    print('Thank you')


def get_choice():
    choice = input(">>>").upper()
    while choice not in ["G", "P", "S", "Q"]:
        choice = input(">>>").upper()
    return choice


def show_stars(score):
    print("*" * score)


def get_score():
    score = float(input('Enter score: '))
    while score < 0 or score > 100:
        print("Invalid")
        score = float(input('Enter score: '))
    return score


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


