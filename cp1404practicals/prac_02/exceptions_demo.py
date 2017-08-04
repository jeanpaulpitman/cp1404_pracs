"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? when the user enters a value other than an integer.
2. When will a ZeroDivisionError occur? when the user enter a zero into the denominator input.
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Yes
"""

# valid_input = False
# while not valid_input:
#     try:
#         numerator = int(input("Enter the numerator: "))
#         denominator = int(input("Enter the denominator: "))
#         if numerator <= 0 or denominator <= 0:
#             print("Please choose values greater than zero")
#         else:
#             fraction = numerator / denominator
#             print(fraction)
#             valid_input = True
#     except ValueError:
#         print("Numerator and denominator must be valid numbers!")
# print("Finished.")

NUMERATOR_TEXT = "numerator"
DENOMINATOR_TEXT = "denominator"


def main():
    numerator = get_positive_int(NUMERATOR_TEXT)
    denominator = get_positive_int(DENOMINATOR_TEXT)
    fraction = numerator / denominator
    print(fraction)
    print("Finished.")


def get_positive_int(purpose):
    valid_int = False
    while not valid_int:
        try:
            selected_number = int(input('Enter the {}: '.format(purpose)))
            if selected_number <= 0:
                print("Please choose a number greater than zero")
            else:
                return selected_number
        except ValueError:
            print("That is not a number, Please choose a number greater than zero")

main()
