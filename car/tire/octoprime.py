from tire.tire import Tire


class Octoprime(Tire):
    def __init__(self, tire_wear:list):
            self.tire_wear = tire_wear
    
    def needs_service(self):
          return sum(self.tire_wear)>=3