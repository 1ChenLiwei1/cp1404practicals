class Guitar:

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        return 2024 - self.year  # Assuming the current year is 2024

    def is_vintage(self):
        return self.get_age() >= 50

    def __lt__(self, other):
        return self.year < other.year