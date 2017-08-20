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
NUMBERS_IN_QUICK_PICK = 6


def main():
    valid_input = False
    while not valid_input:
        try:
            number_of_quick_picks = int(input("How many quick picks? "))
            if number_of_quick_picks <= 0:
                print("Please enter a number greater that zero")
            else:
                valid_input = True
        except ValueError:
            print("That is not a valid integer, try again")

    for i in range(number_of_quick_picks):
        used_numbers = []
        for j in range(NUMBERS_IN_QUICK_PICK):
            random_number = random.randint(MIN_RANGE, MAX_RANGE)
            while random_number in used_numbers:
                random_number = random.randint(MIN_RANGE, MAX_RANGE)
            used_numbers.append(random_number)
        used_numbers.sort()
        for number in used_numbers:
            print("{:2}".format(number), end=' ')
        print()


main()
