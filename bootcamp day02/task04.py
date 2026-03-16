from task03 import Athlete
class Competition:
    
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError(f"{name} is  a string")

        self.name = name              
        self.athletes = []
        self.rankings = {}       

    
    def add_athlete(self, athlete):
        if not isinstance(athlete, Athlete):
            raise TypeError("athlete must be an Athlete instance")
        
        if athlete in self.athletes:
            return

        self.athletes.append(athlete)
    
    def exclude(self, athlete):
        if athlete in self.athletes:
            self.athletes.remove(athlete)

    
    def rank(self, athlete, rank):
        if athlete not in self.athletes:
            raise ValueError("Athlete not engaged in competition")

        
        if not isinstance(rank, int) or rank < 1:
            raise ValueError("Rank must be an integer >= 1")


        athlete.add_record(self.name, rank)

    def print(self):
        if not self.athletes:
            print(f"The {self.name} has no athlete.")
            return

        print(f"athlete(s) engaged in the {self.name}:")

       
        sorted_athletes = sorted(self.athletes, key=lambda a: a._name.lower())

        for athlete in sorted_athletes:
            print(f"{athlete._name} ({athlete._birthdate}) from {athlete._country}")


