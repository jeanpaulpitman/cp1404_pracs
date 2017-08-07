in_file = open('temp.txt')
for line in in_file:
    words = line.split()
    for word in words:
        if word == word_to_find:
            count =+ 1
