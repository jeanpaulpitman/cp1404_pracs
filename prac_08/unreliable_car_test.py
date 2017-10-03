from prac_08.unreliable_car import UnreliableCar


def main():
    """Test code for Taxi class."""
    my_bomb = UnreliableCar("Crappy 1", 100, 40)
    print("Initial values for my_bomb")
    print("fuel =", my_bomb.fuel)
    print("odo =", my_bomb.odometer)
    print("Attempt to Drive 40KM, drive may fail, my_bomb is crappy.")
    my_bomb.drive(40)
    print("fuel =", my_bomb.fuel)
    print("odo =", my_bomb.odometer)
    print("Attempt to Drive 100KM, seems like a bad idea.")
    my_bomb.drive(100)
    print("fuel =", my_bomb.fuel)
    print("odo =", my_bomb.odometer)
    print(my_bomb)



main()