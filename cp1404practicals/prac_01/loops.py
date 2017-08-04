for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

# first attempt
for i in reversed(range(1, 21)):
    print(i, end=' ')
print()

# second attempt
for i in (range(20, 0, -1)):
    print(i, end=' ')
print()
