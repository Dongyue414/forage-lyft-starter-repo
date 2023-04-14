import unittest
import sys 
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from tire.carrigan import Carrigan
from tire.octoprime import Octoprime


class TestTires(unittest.TestCase):
    def test_carrigan_needs_service(self):
        tire_wear = [0.1, 0.3, 0.2, 0.9]
        tires = Carrigan(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_carrigan_not_needs_service(self):
        tire_wear = [0.1, 0.2, 0.4, 0.2]
        tires = Carrigan(tire_wear)
        self.assertFalse(tires.needs_service())

    def test_octoprime_needs_service(self):
        tire_wear = [0.9, 0.9, 0.9, 0.9]
        tires = Octoprime(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_octoprime_not_needs_service(self):
        tire_wear = [0.1, 0.2, 0.4, 0.2]
        tires = Octoprime(tire_wear)
        self.assertFalse(tires.needs_service())     


if __name__ == '__main__':
    unittest.main()