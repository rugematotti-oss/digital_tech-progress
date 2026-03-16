import unittest
from task03 import Athlete
from task04 import Competition
class Testcompetition ( unittest . TestCase ) :
    def test_competition_creation ( self ) :
        comp = Competition (" World Championship ")
        self.assertEqual ( comp.name," World Championship ")
        self.assertEqual ( comp.rankings , {} )
class Testadd_athlete(unittest.TestCase):
    def test_add_athlete(self):
        comp = Competition(" World Championship ")

        athlete1 = Athlete("Athlete 1", "USA", "2000-01-01")
        athlete2 = Athlete("Athlete 2", "France", "2001-01-01")

        comp.add_athlete(athlete1)
        comp.add_athlete(athlete2)

        self.assertEqual(comp.athletes, [athlete1, athlete2])       
if __name__ == "__main__":
    unittest . main ()