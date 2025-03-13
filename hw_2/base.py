from abc import ABC
from hw_2 import exceptions
class Vehicle(ABC):
    def __init__(self,weight, fuel, fuel_consumption):
        self.weight=weight
        self.fuel=fuel
        self.fuel_consumption=fuel_consumption
        self.started=False
    def start(self):
        if not self.started:
            try:
                if self.fuel <= 0:
                    raise exceptions.LowFuelError()
                else:
                    self.started = True
                    return "Машина завелась"
            except exceptions.LowFuelError as e:
                raise e
        else:
            return "Машина уже заведена"

    def move(self, distance):
        if not self.started:
            return f'машина не завелась'
        else:
            fuel_needed = self.fuel_consumption * distance
            try:
                if self.fuel < fuel_needed:
                    raise exceptions.NotEnoughFuel()
                else:
                    self.fuel -= fuel_needed
                    return self.fuel
            except exceptions.NotEnoughFuel as e:
                raise e




