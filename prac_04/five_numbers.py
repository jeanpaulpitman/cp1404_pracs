"""
CP1404/CP5632 Practical
Write a program that asks user for 5 numbers then displays fun facts using min, max
"""


def main():
    """Display income report for incomes over a given number of months."""
    five_numbers = []
    number_count = 5

    for number in range(1, number_count + 1):
        user_number = float(input("Number: "))
        five_numbers.append(user_number)

    print_fun_facts(five_numbers)


def print_fun_facts(five_numbers):
    print("The first number is {:.0f}".format(five_numbers[0]))
    print("The last number is {:.0f}".format(five_numbers[-1]))
    print("The smallest number is {:.0f}".format(min(five_numbers)))
    print("The largest number is {:.0f}".format(max(five_numbers)))
    print("The average of the numbers is {:.1f}".format(sum(five_numbers) / len(five_numbers)))


main()
