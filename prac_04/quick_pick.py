"""
CP1404/CP5632 Practical
Quick pick lottery ticket generator.
Ask user for number of quick picks
print random integers x 6 with no repeat numbers on a line,
display numbers smallest to biggest
"""

import random

MIN_RANGE = 1
MAX_RANGE = 45
QUICK_PICK_LENGTH = 6


def main():
    valid_input = False
    while not valid_input:
        try:
            quick_pick_count = int(input("How many quick picks? "))
            if quick_pick_count <= 0:
                print("Please enter a number greater that zero")
            else:
                valid_input = True
        except ValueError:
            print("That is not a valid integer, try again")

    display_quick_picks(quick_pick_count)


def display_quick_picks(quick_pick_count):
    """Print out 6 random numbers with no duplicates, smallest to biggest."""
    for i in range(quick_pick_count):
        used_numbers = []
        for j in range(QUICK_PICK_LENGTH):
            random_number = random.randint(MIN_RANGE, MAX_RANGE)
            while random_number in used_numbers:
                random_number = random.randint(MIN_RANGE, MAX_RANGE)
            used_numbers.append(random_number)
        used_numbers.sort()
        for number in used_numbers:
            print("{:2}".format(number), end=' ')
        print()


main()
