from battery.battery import Battery
from utils import add_years_to_date

class Spindler_battery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        service_threshold_date = add_years_to_date(self.last_service_date, 2)
        return service_threshold_date < self.current_date