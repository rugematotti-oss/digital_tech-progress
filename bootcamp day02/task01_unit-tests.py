import unittest     
from task01 import Athlete
class TestAthlete ( unittest . TestCase ) :
    def test_athlete_creation ( self ) :
        athlete = Athlete (" Bobby Bob ", " Bolivia ", " 1998 -09 -09 ")
        self . assertEqual ( athlete . name , " Bobby Bob ")
        self . assertEqual ( athlete . country , " Bolivia ")
        self . assertEqual ( athlete . birthdate , " 1998 -09 -09 ")

class Testadd_record ( unittest . TestCase ) :
    def test_add_record ( self ) :
        athlete = Athlete (" Bobby Bob ", " Bolivia ", " 1998 -09 -09 ")
        athlete . add_record (" La Paz Championship ", 2)
        self . assertEqual ( athlete . records , [(" La Paz Championship ", 2)] )         
if __name__ == "__main__":
    unittest . main ()