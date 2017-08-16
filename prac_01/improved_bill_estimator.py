#  constants
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
VALID_TARIFFS = (11, 31)


def main():
    print("Welcome to bill estimator'o'matic 9002 bot, lets estimate your power bill n stuff")
    tariff = get_valid_tariff_int()
    used_kwh = get_valid_daily_usage_float()
    billing_days = get_valid_days_int()
    if tariff == 11:
        daily_price = TARIFF_11 * used_kwh
        bill_estimate = daily_price * billing_days
    else:
        daily_price = TARIFF_31 * used_kwh
        bill_estimate = daily_price * billing_days
    print("Estimated bill: $ {:.2f}".format(bill_estimate))


def get_valid_tariff_int():
    valid_input = False
    while not valid_input:
        try:
            selected_number = int(input('Enter your Tariff? 11 or 31:'))
            if selected_number not in VALID_TARIFFS:
                print("That is not a valid Tariff. Please choose either 11 or 31")
            else:
                return selected_number
        except ValueError:
            print("That is not a number, Please choose either 11 or 31")


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

