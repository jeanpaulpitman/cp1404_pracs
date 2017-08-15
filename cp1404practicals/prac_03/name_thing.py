def main():
    user_name = ""
    while user_name == "":
        print("Please enter your name")
        user_name = input("Name: ")
    print(user_name[::2])

main()
