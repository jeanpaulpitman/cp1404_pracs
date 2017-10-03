"""Module."""
from prac_08.car import Car
from random import randrange


class UnreliableCar(Car):
    """Class."""

    def __init__(self, name, fuel, reliability):
        """Initialize the UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        chance_to_fail = randrange(100)
        if chance_to_fail >= self.reliability:
            distance = 0
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance
