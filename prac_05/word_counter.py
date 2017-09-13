"""
CP1404/CP5632 Practical
Count the occurrences of words in a given string.
"""

text = "this is a collection of words of nice words this is a fun thing it is"
# text = input("Enter your text: ")
words = text.split()
found_words = {}
for word in words:
    try:
        count = found_words[word]
    except KeyError:
        found_words[word] = 1

sorted_words = list(found_words.keys())
sorted_words.sort()
max_length = max((len(word) for word in sorted_words))
for word in sorted_words:
    print("{:{}} : {}".format(word, max_length, found_words[word]))

