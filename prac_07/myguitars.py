import csv
from guitar import Guitar


def main():
    """Main function to run the guitar program."""
    guitars = load_guitars('guitars.csv')
    display_guitars(guitars)

    print("\nSorted guitars (by year):")
    guitars.sort()
    display_guitars(guitars)

    add_new_guitars(guitars)
    save_guitars('guitars.csv', guitars)


def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


def add_new_guitars(guitars):
    print("\nAdd new guitars (leave name empty to stop):")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))


def save_guitars(filename, guitars):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


if __name__ == "__main__":
    main()
