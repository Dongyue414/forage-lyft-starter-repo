from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import Spindler_battery


class Glissade(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, current_date):
        self.engine = WilloughbyEngine(current_mileage, last_service_mileage, current_date)
        self.battery = Spindler_battery(last_service_date)
        super().__init__(self.engine, self.battery)

    def needs_service(self):
        return super().needs_service()