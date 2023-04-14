import unittest
import sys 

sys.path.append("..") 
sys.path.append("..\..")

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

from utils import add_years_to_date
from datetime import date

class TestBattery(unittest.TestCase):
    def test_spindler_battery_needs_service(self):
        last_service_data = add_years_to_date(date.today(),-4)
        current_date = date.today()
        battery = SpindlerBattery(last_service_data, current_date)

        self.assertTrue(battery.needs_service())

    def test_spindler_battery_not_needs_service(self):
        last_service_data = add_years_to_date(date.today(),-1)
        current_date = date.today()
        battery = SpindlerBattery(last_service_data, current_date)

        self.assertFalse(battery.needs_service())

    def test_nubbin_battery_needs_service(self):
        last_service_data = add_years_to_date(date.today(),-5)
        current_date = date.today()
        battery = NubbinBattery(last_service_data, current_date)

        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_not_needs_service(self):
        last_service_data = add_years_to_date(date.today(),-1)
        current_date = date.today()
        battery = SpindlerBattery(last_service_data, current_date)

        self.assertFalse(battery.needs_service())



if __name__ == '__main__':
    unittest.main()
