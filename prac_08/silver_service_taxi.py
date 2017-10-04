"""Module."""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Class."""
    price_per_km = Taxi.price_per_km
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Taxi but with falgfall details."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip including the flagfall."""
        return super().get_fare() + self.flagfall
