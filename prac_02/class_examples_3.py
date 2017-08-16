def main():
    number = 0
    valid_input = False
    while not valid_input:
        try:
            number = int(input("Please enter a number: "))
            if number <= 0:
                print("Number must be greater than 0")
            else:
                valid_input = True
        except ValueError:
            print("Invalid input. Please enter a number")
    print("The square of {} is {}".format(number, square_number(number)))


def square_number(number):
    return number**2


main()
