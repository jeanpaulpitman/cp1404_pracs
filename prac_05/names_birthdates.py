"""
CP1404/CP5632 Practical
Ask user for names and birth dates for five people
Display each persons name and age in years.
"""
import datetime

NAME_COUNT = 5
AVG_DAYS_YEAR = 365.25


def main():
    names_to_dobs = {}
    valid_records_count = 0
    while valid_records_count < NAME_COUNT:
        name = input("Name: ").title()
        list_dob = input("DD/MM/YYYY:").split("/")
        list_dob_int = [int(dob) for dob in list_dob]
        names_to_dobs[name] = list_dob_int
        valid_records_count += 1
    for name in names_to_dobs:
        dob = names_to_dobs[name]
        born = datetime.datetime(dob[2], dob[1], dob[0])
        age_days = (datetime.datetime.now() - born)
        age_days_int = int(age_days.days)
        age_years = age_days_int / AVG_DAYS_YEAR
        print("{:{}} is {:2.0f} years old".format(name, len(name), age_years))


main()
