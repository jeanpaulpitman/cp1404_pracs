"""CP1404/CP5632 Practical - car driving sim."""
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


CHOOSE = "c"
DRIVE = "d"
QUIT = "q"
MENU = """{})uit,{})hoose taxi, {})rive""".format(QUIT, CHOOSE, DRIVE)


def main():
    """Main."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_bill = 0
    print("Let's Drive")
    print(MENU)
    menu_selection = input(">>> ").lower()
    while menu_selection != QUIT:
        if menu_selection == CHOOSE:
            display_taxis(taxis)
            taxi_index = get_positive_number("Choose Taxi: ")
            current_taxi = taxis[taxi_index]
            current_bill += current_taxi.get_fare()

        elif menu_selection == DRIVE:
            distance = get_positive_number("Drive how far? ")
            current_taxi.drive(distance)
            current_bill += current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))

        else:
            print("Invalid menu choice, try again.")
        print("Bill to date: ${:.2f}".format(current_bill))
        print(MENU)
        menu_selection = input(">>>").lower()
    print("Total trip cost ${:.2f}".format(current_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def get_positive_number(hint):
    """Prompt user until positive integer received, return users_number."""
    valid_number = False
    while not valid_number:
        try:
            users_number = int(input(hint))
            if users_number < 0:
                print("Number must be >= 0")
            else:
                return users_number
        except ValueError:
            print("Invalid input; enter a valid number")


main()
