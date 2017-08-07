"""Pass Session activity
Create a program that asks user for a word
then count how many times the word appears in a text file.
Print the result with correct text formatting.
In this example the text file contains the Australia National Anthem"""
TEXT_FILE = "text.txt"

print("Welcome to JP's word counter 9001")
print("Today's file contains the Australian National Anthem")
in_file = open(TEXT_FILE, 'r')
for line in in_file:
    print(line)
in_file.close()

WORD_TO_FIND = input("Please enter the word to find: ")
count = 0
in_file = open(TEXT_FILE, 'r')
for line in in_file:
    line_words = line.split()
    for word in line_words:
        if word.lower() == WORD_TO_FIND.lower():
            count += 1
print(" The word '{}' appears {} times in file '{}'".format(WORD_TO_FIND, count, TEXT_FILE))
in_file.close()
