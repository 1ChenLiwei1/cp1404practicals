from musician import Musician


class Band:
    """Band class"""

    def __init__(self, name=''):
        """Construct a Band with a name and empty member collection."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({', '.join([Musician.__str__(member) for member in self.members])})"

    def add(self, member):
        """Add a member to member collection."""
        self.members.append(member)

    def play(self):
        """Return a string showing every member in band playing their first (or no) instrument."""
        return '\n'.join([Musician.play(member) for member in self.members])
