"""
Pass Session activity
Create a program that prints each letter in the string "Trick or treat" on a new line and backwards
"""

print("Welcome to JP's backwards string reader 9001")
my_string = "Trick or Treat"
for kind in reversed(my_string):
    print(kind)

name = "Cameron"
TAB = 73.6

print("{} has ${:.2f}".format(name, TAB))

print()

NAME_FILE = "name.txt"


"""Get the users name, and write to file."""
out_file = open(NAME_FILE, 'w')
name = input("Please enter your name:")
print(name, file=out_file)
out_file.close()

"""Open the file and read and print the name."""
in_file = open(NAME_FILE, 'r')
name = in_file.read().strip()
print("Your name is {}".format(name))
in_file.close()
