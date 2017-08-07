"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""
MIN_LOWER = 2
MIN_UPPER = 2
MIN_DIGIT = 2
MIN_SPECIAL = 1
MIN_LENGTH = 7
MAX_LENGTH = 10
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between {} and {} characters, and contain:".format(MIN_LENGTH, MAX_LENGTH))
    print("\t{} or more uppercase characters".format(MIN_UPPER))
    print("\t{} or more lowercase characters".format(MIN_LOWER))
    print("\t{} or more numbers".format(MIN_DIGIT))
    if SPECIAL_CHARS_REQUIRED:
        print("\tand {} or more special characters: {}".format(MIN_SPECIAL, SPECIAL_CHARACTERS))
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {} character password is valid: {}".format(len(password), password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        # TODO: count each kind of character (use str methods like isdigit)
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1

    # TODO: if any of the 'normal' counts are zero, return False
    if count_lower < MIN_LOWER or count_upper < MIN_UPPER or count_digit < MIN_DIGIT:
        return False

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero
    if SPECIAL_CHARS_REQUIRED:
        if count_special < MIN_SPECIAL:
            return False

    # if we get here (without returning False), then the password must be valid
    return True


main()
