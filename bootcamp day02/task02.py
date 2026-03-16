class Athlete:
    def __init__(self, name, country, birthdate):
        self._name = name
        self._country = country
        self._birthdate = birthdate
        self._records = []

    def add_record(self, championship_name, rank):
        self._records.append((championship_name, rank))

    def print(bob):
        print(f"My name is : {bob._name}, from {bob._country}")
        print(f"Birthdate: {bob._birthdate}")
        print("My records:")
        if not self._records:
            print("  No records yet")
        else:
            for champ, rank in self._records:
                print(f"  {champ}: Rank {rank}")



