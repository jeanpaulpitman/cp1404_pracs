"""
CP1404/CP5632 Practical
Revisit of prac_01, Electricity bill estimator
refactor to include a dictionary for tariffs.
add three additional tariffs.
"""

VALID_TARIFFS = {11: 0.244618, 31: 0.136928, 44: 0.444444, 47: 0.4747474, 69: 0.696969}


def main():
    print("Welcome to bill estimator'o'matic 9003 bot, lets estimate your power bill n stuff")
    tariffs = {str(tariff) for tariff in VALID_TARIFFS}
    tariff = get_valid_tariff_int(tariffs)
    used_kwh = get_valid_daily_usage_float()
    billing_days = get_valid_days_int()
    bill_estimate = estimate_bill(tariff, used_kwh, billing_days)
    print("Estimated bill: ${:.2f}".format(bill_estimate))


def estimate_bill(tariff, used_kwh, billing_days):
    daily_price = VALID_TARIFFS[tariff] * used_kwh
    bill_estimate = daily_price * billing_days
    return bill_estimate


def get_valid_tariff_int(tariffs):
    tariffs_text = ", ".join(tariffs)
    valid_input = False
    while not valid_input:
        try:
            selected_number = int(input('Enter your Tariff? {}:'.format(tariffs_text)))
            if selected_number not in VALID_TARIFFS.keys():
                print("That is not a valid Tariff. Please choose from: {}.".format(tariffs_text))
            else:
                return selected_number
        except ValueError:
            print("That is not a number, Please choose from: {}.".format(tariffs_text))


def get_valid_daily_usage_float():
    valid_input = False
    while not valid_input:
        try:
            selected_number = float(input('Enter daily use in kWh:'))
            if selected_number <= 0:
                print("Please choose a number greater than zero")
            else:
                return selected_number
        except ValueError:
            print("That is not a number, Please choose a number greater than zero")


def get_valid_days_int():
    valid_input = False
    while not valid_input:
        try:
            selected_number = int(input('Enter number of billing days:'))
            if selected_number <= 0:
                print("Please choose a number greater than zero")
            else:
                return selected_number
        except ValueError:
            print("That is not a number, Please choose a number greater than zero")


main()
