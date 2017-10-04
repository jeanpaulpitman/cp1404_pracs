from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test code for Taxi class."""
    my_taxi_1 = SilverServiceTaxi("Hummer", 200, 4)
    print(my_taxi_1)
    my_taxi_2 = SilverServiceTaxi("Supra", 80, 2)
    my_taxi_2.drive(18)
    print(my_taxi_2)
    print("Fare = ${:.2f}".format(my_taxi_2.get_fare()))



main()
