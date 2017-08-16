"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.

Refactored to include used defined word sequence with error checking
"""
import random

VOWELS = "aeiou".split()
CONSONANTS = "bcdfghjklmnpqrstvwxyz".split()
CHOICES = "%#abcdefghijklmnopqrstuvwxyz".split()
RULES = """Enter the word format using any combination of:
'%' for random Vowels and # for random Consonants
 or mix it up with any alphabet characters too
 EG:'###%%#ville'"""


def main():
    print("Welcome to JP's Random word generator 9002")
    print(RULES)
    valid_format = False
    while not valid_format:
        try:
            word_format = input("Format: ").lower()
            if is_valid_format(word_format):
                word = return_generated_word(word_format)
                print(word)
            else:
                return False
        except ValueError:
            print("That is not a valid character, try again")


def is_valid_format(word_format):
    for character in word_format:
        if character not in CHOICES:
            return False
    return True


def return_generated_word(word_format):
    generated_word = ""
    for character in word_format:
        if character == "#":
            generated_word += random.choice(CONSONANTS)
        elif character == "%":
            generated_word += random.choice(VOWELS)
        else:
            generated_word += character
    return generated_word

main()
