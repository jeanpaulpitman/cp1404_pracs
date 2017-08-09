def main():
    age = 0
    valid_input = False
    while not valid_input:
        try:
            age = int(input("Please enter your age: "))
            if age <= 0:
                print("Age must be greater than 0")
            elif age >= 100:
                print("Wow you are really old")
                valid_input = True
            else:
                valid_input = True
        except ValueError:
            print("Invalid input. Please enter a number")
    if is_even(age) :
        print("{} is an even number".format(age))
    else:
        print("{} is an odd number".format(age))


def is_even(number):
    return number % 2 == 0

main()
