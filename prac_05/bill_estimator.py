"""
CP1404/CP5632 Practical
Revisit of prac01, bill estimator
"""


def main():
    print("Welcome to bill estimator'o'matic 9001 bot, lets estimate your power bill n stuff")
    price_kwh = get_valid_price_int()
    used_kwh = get_valid_daily_usage_float()
    billing_days = get_valid_days_int()

    daily_price = (price_kwh / 100) * used_kwh
    bill_estimate = daily_price * billing_days
    print("Estimated bill: $ {}".format(bill_estimate))


def get_valid_price_int():
    valid_input = False
    while not valid_input:
        try:
            selected_number = int(input('Enter cents per kWh:'))
        except ValueError:
            print("That is not a number, Please choose a number greater than zero")
            continue

        if selected_number <= 0:
            print("Please choose a number greater than zero")
            continue
        else:
            return selected_number


def get_valid_daily_usage_float():
    valid_input = False
    while not valid_input:
        try:
            selected_number = float(input('Enter daily use in kWh:'))
        except ValueError:
            print("That is not a number, Please choose a number greater than zero")
            continue

        if selected_number <= 0:
            print("Please choose a number greater than zero")
            continue
        else:
            return selected_number


def get_valid_days_int():
    valid_input = False
    while not valid_input:
        try:
            selected_number = int(input('Enter number of billing days:'))
        except ValueError:
            print("That is not a number, Please choose a number greater than zero")
            continue

        if selected_number <= 0:
            print("Please choose a number greater than zero")
            continue
        else:
            return selected_number


main()

