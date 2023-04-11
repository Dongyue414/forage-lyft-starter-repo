from car import Car
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import Spindler_battery


class Palindrome(Car):
    def __init__(self, last_service_date, warning_light_is_on):
        self.engine = SternmanEngine(warning_light_is_on)
        self.battery = Spindler_battery(last_service_date)
        super().__init__(self.engine, self.battery)

    def needs_service(self):
        return super.needs_service()