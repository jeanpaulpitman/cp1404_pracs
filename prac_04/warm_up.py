def main():
    numbers = [3, 1, 4, 5, 9, 2]
    print(numbers[0])
    print(numbers[-1])
    print(numbers[3])
    print(numbers[:-1])
    print(numbers[3:4])
    print(5 in numbers)
    print(7 in numbers)
    print("3" in numbers)
    print(numbers + [6, 5, 3])
    numbers[0] = 10
    print(numbers)
    numbers[-1] = 1
    print(numbers)
    some_numbers = numbers[2:]
    print(some_numbers)
    print(9 in numbers)


main()
