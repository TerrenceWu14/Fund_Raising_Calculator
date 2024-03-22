# checks that the user typed yes or no
def yes_no():
    while True:

        # asks the question
        response = input().lower()

        if response == "y" or response == "yes":
            return "yes"

        elif response == "n" or response == "no":
            return "no"

        # prints the error message
        else:
            print("Please enter yes or no\n")


# Main routine goes here
ok = yes_no()
print(ok)
