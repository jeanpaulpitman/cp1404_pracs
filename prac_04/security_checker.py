"""
CP1404/CP5632 Practical
Write a program that asks user for user_name,
checks if user_name is in a list of usernames,
and informs user if access granted or denied.
"""


def main():
    """Checks if username is valid."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
                 'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    user_name = input("Username: ")
    if is_valid_user_name(usernames, user_name):
        print("Access granted")
    else:
        print("Access denied")


def is_valid_user_name(usernames, user_name):
    if user_name in usernames:
        return True
    else:
        return False


main()
