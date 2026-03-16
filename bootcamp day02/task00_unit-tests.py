import unittest
from task00 import getSecondMax, multiply
class TestMultiply ( unittest.TestCase ) :
    def test_multiply_integers ( self ) :
        self.assertEqual ( multiply (3 ,4) ,12)
    def test_multiply_floats ( self ) :
        self.assertAlmostEqual ( multiply (1.5 ,2) ,3.0)

class TestgetSecondMax(unittest.TestCase):
    def test_getSecondMax(self):
        self.assertEqual(getSecondMax([13,56,2,48,9,4]), 48)
        self.assertEqual(getSecondMax([1, 2, 3, 4, 5]), 4)
        with self.assertRaises(ValueError):
            getSecondMax([5,5,5])
if __name__ == "__main__":
    unittest.main ()