import unittest

class TestGetRanking(unittest.TestCase):
    def test_get_ranking(self):
        athlete1 = Athlete("Athlete 1", "USA", "2000-01-01")
        athlete2 = Athlete("Athlete 2", "France", "2001-01-01")
        athlete3 = Athlete("Athlete 3", "Germany", "1999-01-01")

        championship = Championship("World Championship")
        championship.add_athlete(athlete1)
        championship.add_athlete(athlete2)
        championship.add_athlete(athlete3)

        self.assertEqual(championship.get_ranking(athlete1), 2)
        self.assertEqual(championship.get_ranking(athlete2), 1)
        self.assertEqual(championship.get_ranking(athlete3), 3)