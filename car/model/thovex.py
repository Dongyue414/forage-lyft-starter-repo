from car.car import Car
from car.engine.capulet_engine import CapuletEngine
from car.battery.nubbin_battery import NubbinEngine


class Calliope(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.engine = CapuletEngine(current_mileage, last_service_mileage)
        self.battery = NubbinEngine(last_service_date)
        super().__init__(self.engine, self.battery)

    def needs_service(self):
        return super.needs_service()