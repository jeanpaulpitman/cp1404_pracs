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
            print("lIST THE GUITARS")
            list_all_guitars(guitars)
        elif menu_selection == ADD_GUITAR:
            print("ADD THE GUITAR")
        else:
            print("Invalid menu choice, try again.")
        print(MENU)
        menu_selection = input(">>>").upper()
    print("Have a nice day")


def list_all_guitars(guitars):
    print("These are my guitars:")
    guitar_count = 1
    for guitar in guitars:
        if guitar.is_vintage():
            vintage_string = "(Vintage)"
        else:
            vintage_string = ""
        print("Guitar {}: {:>18} ({}), worth $ {:>10.2f} {}".format(guitar_count, guitar.name, guitar.year,
                                                                    guitar.cost, vintage_string))
        guitar_count += 1


main()
