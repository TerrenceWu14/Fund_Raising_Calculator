# checks that the number the user entered is greater than 0
# and whether it is the correct number type
def num_check(question, error, num_type):
    while True:

        try:
            response = num_type(input(question))

            # prints an error if the number is < 0
            if response <= 0:
                print(error)

            # returns the response
            else:
                return response

        # prints the error if its a value error
        except ValueError:
            print(error)


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


# checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        # if the response is blank, outputs the error
        if response == "":
            print("Sorry this can't be blank. Please try again")

        else:
            return response


# Main routine goes here
get_int = num_check("How many do you need?",
                    "Please enter a number more than 0 "
                    "with no decimal points\n",
                    int)

get_cost = num_check("How many do you need?",
                     "Please enter a number more than 0\n",
                     float)
