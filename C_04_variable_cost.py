import pandas


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


# checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        # if the response is blank, outputs the error
        if response == "":
            print("Sorry this can't be blank. Please try again")

        else:
            return response


# currency formatting function
def currency(x):
    return f"${x:.2f}"


# main routine

# sets up dictionaries and lists

item_list = []
quantity_list = []
price_list = []

variable_dict = {
    "Item": item_list,
    "Quantity": quantity_list,
    "Price": price_list,
}




