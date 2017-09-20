"""CP1404/CP5632 Practical - Programming languages."""
from prac_07.guitar import Guitar


LIST_GUITARS = "L"
ADD_GUITAR = "A"
QUIT = "Q"
MENU = """Menu:
{} - List Guitars
{} - Add Guitars
{} - Quit program""".format(LIST_GUITARS, ADD_GUITAR, QUIT)


def main():
    """Main."""
    print("My Guitars!")
    guitars = []
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Flipper 4500", 1812, 256035.40))
    guitars.append(Guitar("Killer 9001", 1984, 6085.88))
    print(MENU)
    menu_selection = input(">>>").upper()
    while menu_selection != QUIT:
        if menu_selection == LIST_GUITARS:
            if len(guitars) == 0:
                print("You have no Guitars to list, try adding some.")
            else:
                list_all_guitars(guitars)
        elif menu_selection == ADD_GUITAR:
            add_guitar(guitars)
        else:
            print("Invalid menu choice, try again.")
        print(MENU)
        menu_selection = input(">>>").upper()
    list_all_guitars(guitars)
    print("Have a nice day")


def list_all_guitars(guitars):
    print("These are my guitars:")
    guitar_count = 1
    for guitar in guitars:
        if guitar.is_vintage():
            vintage_string = "(Vintage)"
        else:
            vintage_string = ""
        print("Guitar {}: {:>18} ({}), worth $ {:>10,.2f} {}".format(guitar_count, guitar.name, guitar.year,
                                                                     guitar.cost, vintage_string))
        guitar_count += 1


def add_guitar(guitars):
    """Prompt user for new guitar details until blank name received."""
    blank_name = False
    while not blank_name:
        name = input("Name:").title()
        if name == "":
            blank_name = True
        else:
            year = get_positive_number("Year:")
            cost = get_positive_float("Cost:")
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            print("{} ({}) : ${:>8.2f} added.".format(new_guitar.name, new_guitar.year, new_guitar.cost))


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


def get_positive_float(hint):
    """Prompt user until positive float received, return users_number."""
    valid_number = False
    while not valid_number:
        try:
            users_number = float(input(hint))
            if users_number < 0:
                print("Number must be >= 0.0")
            else:
                return users_number
        except ValueError:
            print("Invalid input; enter a valid number")


main()
