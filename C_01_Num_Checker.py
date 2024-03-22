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


# Main routine goes here
get_int = num_check("How many do you need?",
                    "Please enter a number more than 0 "
                    "with no decimal points\n",
                    int)


get_cost = num_check("How many do you need?",
                     "Please enter a number more than 0\n",
                     float)



