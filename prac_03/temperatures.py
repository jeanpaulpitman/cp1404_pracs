"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            prompt = "Celsius: "
            celsius = return_valid_float(prompt)
            print("Result: {:.2f} F".format(celsius_to_fahrenheit(celsius)))
        elif choice == "F":
            prompt = "Fahrenheit: "
            fahrenheit = return_valid_float(prompt)
            print("Result: {:.2f} C".format(fahrenheit_to_celsius(fahrenheit)))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


def return_valid_float(prompt):
    valid_float = False
    while not valid_float:
        try:
            return float(input(prompt))
        except ValueError:
            print("That is not a valid float, try again.")

main()
