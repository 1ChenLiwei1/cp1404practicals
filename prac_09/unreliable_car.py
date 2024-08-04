from random import uniform
from car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def drive(self, distance):
        distance_driven = 0
        if uniform(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven

    def __str__(self):
        return f"{super().__str__()}, have {self.reliability}% chance to drive the car."
