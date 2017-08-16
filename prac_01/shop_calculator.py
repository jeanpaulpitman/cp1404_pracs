"""
CP1404/CP5632 - Practical
Create a simple shop calculator
"""
# constants
DISCOUNT_THRESHOLD = 100  # $100
DISCOUNT_RATE = .1  # 10% 


def main():
    print("Welcome to shop bot, lets calculate n stuff")
    number_of_item = get_valid_int()
    item_prices = []
    for i in range(number_of_item):
        price = get_valid_float()
        item_prices.append(price)
    total_price = sum(item_prices)
    if total_price >= DISCOUNT_THRESHOLD:
        discount = total_price * DISCOUNT_RATE
        display_price = total_price - discount
    else:
        display_price = total_price

    print("Total price for {0} items is ${1:.2f}".format(number_of_item, display_price))


def get_valid_int():
    valid_input = False
    while not valid_input:
        try:
            selected_number = int(input('Number of items:'))
        except ValueError:
            print("That is not a number, Please choose a number greater than zero")
            continue

        if selected_number <= 0:
            print("Please choose a number greater than zero")
            continue
        else:
            return selected_number


def get_valid_float():
    valid_input = False
    while not valid_input:
        try:
            selected_number = float(input('Price of item: $'))
        except ValueError:
            print("That is not a number, Please choose a number greater than zero")
            continue

        if selected_number <= 0:
            print("Please choose a number greater than zero")
            continue
        else:
            return selected_number


main()
