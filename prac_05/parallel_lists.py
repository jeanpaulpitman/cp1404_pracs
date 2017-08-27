"""
CP1404/CP5632 Practical
Convert parallel lists into a dictionary.
"""
import datetime


AVG_DAYS_YEAR = 365.25


def main():
    names = ["Jack", "Jill", "Harry"]
    dobs = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]
    names_to_dobs = zip_dictionary(names, dobs)
    for name in names_to_dobs:
        dob = names_to_dobs[name]
        born = datetime.datetime(dob[2], dob[1], dob[0])
        age_days = (datetime.datetime.now() - born)
        age_days_int = int(age_days.days)
        age_years = age_days_int / AVG_DAYS_YEAR
        print("{:{}} is {:2.0f} years old".format(name, len(name), age_years))


def zip_dictionary(list_a, list_b):
    return dict(zip(list_a, list_b))


main()
