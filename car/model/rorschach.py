from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinEngine


class Rorschach(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, current_date):
        self.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery = NubbinEngine(last_service_date, current_date)
        super().__init__(self.engine, self.battery)

    def needs_service(self):
        return super().needs_service()