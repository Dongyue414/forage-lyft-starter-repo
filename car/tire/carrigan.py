from tire.tire import Tire


class Carrigan(Tire):
    def __init__(self, tire_wear:list):
            self.tire_wear = tire_wear
    
    def needs_service(self):
          return any([i > 0.9 for i in self.tire_wear])