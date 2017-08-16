"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# Constants
BONUS_THRESHOLD_AMOUNT = 1000
BONUS_RATE_HIGH = .15
BONUS_RATE_LOW = .1
ZERO = 0

sales = float(input("Enter sales: $"))
while sales >= ZERO:
    if sales >= BONUS_THRESHOLD_AMOUNT:
        bonus = sales * BONUS_RATE_HIGH
        print("Bonus: ${:.2f}".format(bonus))
    elif sales > ZERO:
        bonus = sales * BONUS_RATE_LOW
        print("Bonus: ${:.2f}".format(bonus))
    else:
        print("Please enter a number greater than zero")
    sales = float(input("Enter sales: $"))
print("Thanks for playing")
