import string


def count_letters(my_string):
    """Return the count of letter is a_str."""
    count = 0
    for char in my_string:
        if char.lower() in string.ascii_lowercase:
            count += 1
    return count

