"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    prompt = "Enter score: "
    score = return_valid_float(prompt)
    print("Your score is {}".format(return_result(score)))


def return_result(score):
    if score < 0 or score > 100:
        return "an invalid score, try again"
    elif score >= 90:
        return "Excellent, Keep it up"
    elif score >= 50:
        return "Passable, Lucky you"
    else:
        return "Bad, perhaps you are a bad, see lecturer for assistance"


def return_valid_float(prompt):
    valid_float = False
    while not valid_float:
        try:
            return float(input(prompt))
        except ValueError:
            print("That is not a valid float, try again.")

main()
