NAME_FILE = "name.txt"
NUMBERS_FILE = "numbers.txt"
LONG_NUMBERS_FILE = "long_numbers.txt"

out_file = open(NAME_FILE, 'w')
name = input("Please enter your name:")
print(name, file=out_file)
out_file.close()

in_file = open(NAME_FILE, 'r')
name = in_file.read().strip()
print("Your name is {}".format(name))
in_file.close()

in_file = open(NUMBERS_FILE, 'r')
first_number = in_file.readline()
second_number = in_file.readline()
total = int(first_number) + int(second_number)
print("Your result is {}".format(total))
in_file.close()

out_file = open(LONG_NUMBERS_FILE, 'w')
for i in range(1, 3333, 3):
    print(i, file=out_file)
out_file.close()

in_file = open(LONG_NUMBERS_FILE, 'r')
total = 0
for line in in_file:
    amount = int(line)
    total += amount
print("Your total is: {}".format(total))
in_file.close()
