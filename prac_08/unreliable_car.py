"""Module."""
from prac_08.car import Car
from random import randint


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
        chance_to_fail = randint(0, 100)
        if chance_to_fail >= self.reliability:
            distance = 0
        else:
            distance = super().drive(distance)
        return distance
