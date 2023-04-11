import unittest
import sys 

sys.path.append("..") 
sys.path.append("..\..")

from model.calliope import Calliope
from model.glissade import Glissade
from model.palindrome import Palindrome
from model.rorschach import Rorschach
from model.thovex import Thovex

from utils import add_years_to_date
import datetime

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.date.today()
        last_service_date = add_years_to_date(today, -3)
        current_mileage = 0
        last_service_mileage = 0
        
        car = Calliope(last_service_date, current_mileage, last_service_mileage, today)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.date.today()
        last_service_date = add_years_to_date(today, -1)
        current_mileage = 0
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage, today)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.date.today()
        last_service_date = datetime.date.today()
        current_mileage = 30001
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage, today)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.date.today()
        last_service_date = datetime.date.today()
        current_mileage = 30000
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage, today)
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()