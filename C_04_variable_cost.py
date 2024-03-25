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
quant_list = []
price_list = []
cost_list = []

variable_dict = {
    "Item": item_list,
    "Quantity": quant_list,
    "Price": price_list,
    "Cost": cost_list,

}

while True:
    # gets the item, quantity, price and cost of each item
    item = not_blank("Item: ")

    # breaks out of the loop if the user chooses to end early
    if item.lower() == "xxx":
        break

    quantity = num_check("Quantity: ", "Please enter an whole number:", int)
    price = num_check("Price per item: ", "Please enter a number greater than 0:", float)
    cost = quantity * price

    # appends the inputted values into their lists
    item_list.append(item)
    quant_list.append(quantity)
    price_list.append(price)
    cost_list.append(cost)

# sets up the table of data
data_table = pandas.DataFrame(variable_dict)
data_table = data_table.set_index('Item')


# currency formatting (uses currency function)
add_dollars = ['Price', 'Cost']
# adds the currency formatting to the strings in the list
for var_item in add_dollars:
    data_table[var_item] = data_table[var_item].apply(currency)

print("----------------------")

print(data_table)





