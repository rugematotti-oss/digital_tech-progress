class Athlete:
    def __init__(self, name, country, birthdate):
        
        self.name = name
        self.country = country
        self.birthdate = birthdate
        
        self.records = []

    def add_record(self, championship_name, rank):
        
        self.records.append((championship_name, rank))

    def print(self):
        
        print(f"My name is : {self.name}, from {self.country}")
        print(f"Birthdate: {self.birthdate}")
        print("My records:")
        if not self.records:
            print("  No records yet")
        else:
            for champ, rank in self.records:
                print(f"  {champ}: Rank {rank}")


