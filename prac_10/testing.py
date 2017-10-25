"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_07.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    if n == 1:
        complete_text = s
        return complete_text
    else:
        new_text = []
        for i in range(n):
            new_text.append(s)
        complete_text = ' '.join(new_text)
    return complete_text


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # TODO: 1. fix the repeat_string function above so that it passes the test
    # Hint: "-".join(["yo", "yo"] -> "yo-yo"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # TODO: 2. write assert statements to show if Car sets the fuel correctly
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    test_car = Car(fuel=10)
    assert test_car.fuel == 10
    test_car_2 = Car()
    assert test_car_2.fuel == 0


run_tests()

# TODO: 3. Uncomment the following line and run the doctests
doctest.testmod()

# TODO: 4. Fix the failing is_long_word function
# (don't change the tests, but the function!)

# TODO: 5. Write and test a function to format a phrase as a sentence,
# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests so that:
# 'hello' -> ''Hello.'


def make_sentence(text):
    """
    >>> make_sentence("hello")
    'Hello.'
    >>> make_sentence("it is an ex parrot")
    'It is an ex parrot.'
    >>> make_sentence("welcome to the jungle.")
    'Welcome to the jungle.'
    """
    first_letter = str(text[0]).upper()
    if text[-1] == ".":
        last_letter = ""
    else:
        last_letter = "."
    new_sentence = first_letter + text[1:] + last_letter
    return new_sentence



# 'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more you decide (that's valid!)
# then write the body of the function so that the tests pass
