LOWER = 33
UPPER = 127
character = input("Enter a character: ")
ascii_code = ord(character)
print("The ASCII code for {} is {}".format(character, ascii_code))

number = int(input("Enter a number between 33 and 127: "))
while number < LOWER or number > UPPER:
    print("Invalid number")
    number = int(input("Enter a number between 33 and 127: "))
ascii_char = chr(number)
print("The character for {} is {}".format(number, ascii_char))

column = 0
number_of_columns = int(input("Enter number of columns between 0 and 95: "))
while number_of_columns < 0 or number_of_columns > 95:
    print("Invalid number of columns")
print("Column Number : ASCII Number : ASCII Character")
for i in range(0, number_of_columns, 1):
    column = column + 1
    ascii_char = chr(i+33)
    print("{}   {}   {}".format(column, i+33, ascii_char))
