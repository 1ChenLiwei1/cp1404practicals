from guitar import Guitar


def main():
    guitars = []
    print("My guitars !")
    guitar_name = input("Name:")
    while guitar_name:
        guitar_year, guitar_cost = get_data()
        guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        print(f"{guitar} added.")
        guitars.append(guitar)
        guitar_name = input("Name:")
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("These are my guitars:")
    max_name = max(len(guitar.name) for guitar in guitars)
    max_cost = max(len(str(guitar.cost)) for guitar in guitars)
    for i, guitar in enumerate(guitars,1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>{max_name}} ({guitar.year}), worth ${guitar.cost:{max_cost+2},.2f}{vintage_string}")


def get_data():
    guitar_year = float(input("Year:"))
    guitar_cost = float(input("Cost: $"))
    return guitar_year, guitar_cost


main()
