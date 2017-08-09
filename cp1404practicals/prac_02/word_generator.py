"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
CHOICES = "%#abcdefghijklmnopqrstuvwxyz"


def main():
    print("Welcome to JP's Random word generator 9001")
    print("Enter the word length, we do the rest")
    word_length = int(input("Word length: "))
    word_format = get_random_format(word_length)
    word = ""
    for kind in word_format:
        if kind == "#":
            word += random.choice(CONSONANTS)
        elif kind == "%":
            word += random.choice(VOWELS)
        else:
            word += kind

    print(word)


def get_random_format(word_length):
    random_format = ""
    for i in range(word_length):
        random_format += random.choice(CHOICES)
    return random_format


main()
