def main():
    user_name = get_name()
    print(return_characters(user_name, get_frequency()))


def return_characters(user_name, frequency):
    return user_name[::frequency]


def get_name():
    user_name = ""
    while user_name == "":
        print("Please enter your name")
        user_name = input("Name: ")
    return user_name


def get_frequency():
    letter_frequency = 0
    while letter_frequency == 0:
        try:
            print("Please enter letter frequency")
            letter_frequency = int(input("Frequency: "))
        except ValueError:
            print("That is not a number, please enter a number")
    return letter_frequency

main()
