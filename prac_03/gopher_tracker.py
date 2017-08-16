"""
CP1404/CP5632 - Practical
GPS (Gopher Population Simulator).
Starting population 1000
each year population increases randomly by 10% - 20%
each year population decreases randomly by 5% - 25%
Population is tracked for 10 years
"""
import random
DURATION = 10
MAX_BIRTHS = 0.2  # 20%
MIN_BIRTHS = 0.1  # 10%
MAX_DEATHS = 0.25  # 25%
MIN_DEATHS = 0.05  # 5%
INITIAL_POP = 1000
WELCOME = """Welcome to the Gopher Population Simulator!"""


def main():
    population = INITIAL_POP
    print(WELCOME)
    print("Starting population: {}".format(INITIAL_POP))

    for i in range(DURATION):
        pop_increase = population * random.uniform(MIN_BIRTHS, MAX_BIRTHS)
        pop_decrease = population * random.uniform(MIN_DEATHS, MAX_DEATHS)
        population = population + pop_increase - pop_decrease
        print("""Year {}
****
{:.0f} gophers were born, {:.0f} died.
Population: {:.0f}

""".format(i+1, pop_increase, pop_decrease, population))

main()
