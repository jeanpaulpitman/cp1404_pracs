def get_valid_number():
    valid_input = False
    while not valid_input:
        try:
            selected_number = int(input('Number of items:'))
            valid_input = True
            return selected_number
        except ValueError:
            print("That is not a number, Please choose a number greater than zero")
        except selected_number < 1:
            print("Please choose a number greater than zero")
