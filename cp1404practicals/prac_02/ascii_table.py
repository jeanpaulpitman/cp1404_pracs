ASCII_MIN = 33
ASCII_MAX = 127


def main():
    user_char = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(user_char, ord(user_char)))

    user_number = get_valid_ascii_int()
    print("The character for {} is {}".format(user_number, chr(user_number)))

    print("Congratulations here is the full ASCII table as a reward")
    for i in range(ASCII_MIN, ASCII_MAX + 1):
        print("{:>3}{:>8}".format(i, chr(i)))


def get_valid_ascii_int():
    valid_input = False
    while not valid_input:
        try:
            selected_number = int(input("Enter a number between {} and {}:".format(ASCII_MIN, ASCII_MAX)))
            if selected_number < ASCII_MIN or selected_number > ASCII_MAX:
                print("That is not a valid ASCII number, choose a number between {} and {}:".format(ASCII_MIN, ASCII_MAX))
            else:
                return selected_number
        except ValueError:
            print("That is not a number, Please choose a number between {} and {}:".format(ASCII_MIN, ASCII_MAX))

main()
