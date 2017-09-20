"""CP1404/CP5632 Practical - Guitar activity, test."""
from prac_07.guitar import Guitar


def main():
    """Main."""
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Flipper 4500", 1812, 256035.40)
    guitar3 = Guitar("Killer 9001", 1984, 6085.88)

    print(guitar1)
    print(guitar2)
    print(guitar3)

    print("Expected 95 got {}".format(guitar1.get_age()))
    print("Expected 205 got {}".format(guitar2.get_age()))
    print("Expected 33 got {}".format(guitar3.get_age()))
    print("Expected True got {}".format(guitar1.is_vintage()))
    print("Expected True got {}".format(guitar2.is_vintage()))
    print("Expected False got {}".format(guitar3.is_vintage()))


main()
