import csv

def main():
    filename = 'wimbledon.csv'
    data = read_data(filename)
    champion_counts = count_champions(data)
    countries = get_countries(data)
    display_results(champion_counts, countries)


def display_results(champion_counts, countries):
    print("Wimbledon Champions:")
    for champion, count in champion_counts.items():
        print(f"{champion} {count}")

    print("\nThese countries have won Wimbledon:")
    print(", ".join(countries))


def get_countries(data):
    countries = {row[1] for row in data}
    return sorted(countries)


def count_champions(data):
    champion_counts = {}
    for row in data:
        champion = row[2]
        if champion in champion_counts:
            champion_counts[champion] += 1
        else:
            champion_counts[champion] = 1
    return champion_counts


def read_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        csv_reader = csv.reader(filename)
        next(csv_reader)
        data = [row for row in csv_reader]
        return data


