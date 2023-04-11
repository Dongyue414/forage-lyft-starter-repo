from car import Car
from engine.capulet_engine import CapuletEngine
from battery.nubbin_battery import NubbinBattery


class Thovex(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, current_date):
        self.engine = CapuletEngine(current_mileage, last_service_mileage)
        self.battery = NubbinBattery(last_service_date, current_date)
        super().__init__(self.engine, self.battery)

    def needs_service(self):
        return super().needs_service()