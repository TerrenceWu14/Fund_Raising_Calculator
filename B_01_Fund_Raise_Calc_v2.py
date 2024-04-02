import pandas
import re
import math


# displays instructions
def instructions():
    print('''

*** Instructions ***

To begin, type in the name of the product and how many of it you are
planning to make or sell.

Then, enter any costs you expect for things like materials or labour,
making sure to include how many items you need and the price for each.
If you have any fixed costs, like rent or equipment, let the program know.

When you have entered all your fixed/variable costs type "xxx" to exit.

After that enter the profit target in percentages or in dollars and then
we'll recommend you the selling price and the minimum price. 

When you finish, all the data will be sorted into tables that are saved
onto a txt file for you to use as well as in the console.

        ''')


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
def yes_no(question):
    while True:
        response = input(question)
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


# currency formatting function
def currency(x):
    return f"${x:.2f}"


# creates the table for all the expenses
def get_expenses(var_fixed):
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
        print()

        # gets the price, cost and quantities
        if var_fixed == "variable":
            quantity = num_check("Quantity: ", "Please enter a whole number:", int)
        else:
            quantity = 1

        print()
        price = num_check("Price per item: ", "Please enter a number greater than 0:", float)
        cost = quantity * price

        # appends the inputted values into their lists
        item_list.append(item)
        quant_list.append(quantity)
        price_list.append(price)
        cost_list.append(cost)
        print()

    # sets up the table of data
    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # currency formatting (uses currency function)
    add_dollars = ['Price', 'Cost']

    # finds subtotal
    sub_total = expense_frame['Cost'].sum()

    # adds the currency formatting to the strings in the list
    for var_item in add_dollars:
        expense_frame[var_item] = expense_frame[var_item].apply(currency)

    return [expense_frame, sub_total]


# rounding function
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


# prints expense frames
def expense_print(heading, frame, subtotal):
    print()
    print(f"***** {heading} Costs *****")
    print(frame)
    print()
    print(f"{heading} Costs: ${subtotal:.2f}")
    return ""


# calculates the profit goal
def profit_goal(total_cost):
    while True:

        # asks the user for the profit goal
        response = input("Profit Goal? ")

        # the allowed string pattern (allows only integers above 0
        # with $ at the start or %$ at the end)
        allowed = r'^[$]?[1-9]\d*(?:\.\d+)?[%$]?$'

        # if the response matches the allowed pattern, returns response
        if re.match(allowed, response):

            # gets the number part of the response, ignores all surrounding characters
            numeric_part = re.search(r'\d*\.?\d+', response).group()

            # converts the percentage the user inputted into a number
            if response.startswith("$"):
                # converts the response to a number
                target_profit = float(numeric_part)

            # converts the percentage the user inputted into a number
            elif response.endswith("%"):
                target_profit = total_cost * (float(numeric_part) / 100)

            else:
                target_profit = float(numeric_part)

            return target_profit

        # else sends the user back to the start of the loop
        else:
            print("Please enter a valid response (a %, a number above 0 or e.g. $500)")


# main routine

# asks the user if they have used the program or not
want_instructions = yes_no("Have you used this program before?")

# displays the instructions if they haven't
if want_instructions == "no":
    instructions()

product_name = not_blank("What is your product name?")
print()
how_many = num_check("How many items will you be producing? ",
                     "The number of items must be a whole number more than 0", int)
print()

# get variable expenses (e.g. products like apples)
print("Please enter your variable (for example: products) costs below: ")
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]
print()

have_fixed = yes_no("Do you have fixed costs (yes or no)?")

if have_fixed == "yes":
    # gets fixed expenses (e.g. stalls/rent)
    print("Please enter your fixed costs (for example: stall hire) below: ")
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]
else:
    fixed_sub = 0
    fixed_frame = ""

# gets the total costs
all_costs = variable_sub + fixed_sub

# gets the profit target
profit_target = profit_goal(all_costs)

# calculates total sales needed to reach goal
sales_needed = all_costs + profit_target

# asks user for rounding
round_to = num_check("Round to nearest...? $",
                     "Can't be 0", int)

# calculates recommended price
selling_price = sales_needed / how_many
recommended_price = round_up(selling_price, round_to)

print(f"***** Fund Raising - {product_name}")

# prints the table of data for variable costs
expense_print("Variable", variable_frame, variable_sub)

if have_fixed == "yes":
    # prints the table of data for fixed costs
    expense_print("Fixed", fixed_frame[['Cost']], fixed_sub)

print()
print("***** Profit and Sales Targets *****")
print(f"Profit Target: ${profit_target:.2f}")
print(f"Total Sales: ${all_costs + profit_target:.2f}")
print()

print()
print("***** Pricing *****")
print(f"Minimum Price: ${selling_price:.2f}")
print(f"Recommended Price ${recommended_price}")

# change dataframe to string (so it can be written to a txt file)
variable_txt = variable_frame.to_string() if isinstance(variable_frame, pandas.DataFrame) else ""
fixed_txt = fixed_frame.to_string() if isinstance(fixed_frame, pandas.DataFrame) else ""

to_write = [product_name, variable_txt, fixed_txt, profit_target,
            recommended_price]

# write to file
# create file to hold data(add .txt extension)
file_name = f"{product_name}.txt"
text_file = open(file_name, "w+")

# heading
for item in to_write:
    text_file.write(str(item))
    text_file.write("\n\n")

# close file
text_file.close()
