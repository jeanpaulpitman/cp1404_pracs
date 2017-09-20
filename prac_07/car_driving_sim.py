"""CP1404/CP5632 Practical - car driving sim."""
from prac_07.car import Car


DRIVE = "d"
REFUEL = "r"
QUIT = "q"
MENU = """Menu:
{}) - Drive
{}) - Refuel
{}) - Quit""".format(DRIVE, REFUEL, QUIT)


def main():
    """Main."""
    print("Let's Drive")
    car_name = input("Enter your car name: ").title()
    player_car = Car(car_name, 100)
    print(player_car)

    print(MENU)
    menu_selection = input("Enter your choice: ").lower()
    while menu_selection != QUIT:
        if menu_selection == DRIVE:
            distance = get_positive_number("How many km do you wish to drive? ")
            traveled = player_car.drive(distance)
            if traveled < distance:
                warning_string = " and ran out of fuel."
            else:
                warning_string = "."
            print("The car drove {}km{}".format(traveled, warning_string))
        elif menu_selection == REFUEL:
            units_fuel = get_positive_number("How many units of fuel do you want to add to the car? ")
            player_car.add_fuel(units_fuel)
            print("Added {} units of fuel.".format(units_fuel))
        else:
            print("Invalid menu choice, try again.")
        print(player_car)
        print(MENU)
        menu_selection = input(">>>").lower()
    print("Good bye {}'s driver.".format(player_car.name))


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
