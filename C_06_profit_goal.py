import re


# checks that the user typed yes or no
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"
        else:
            print("Please enter yes or no\n")


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
                target_profit = total_cost * (float(numeric_part[:-1]) / 100)
            else:
                target_profit = float(numeric_part)

            return target_profit

        # else sends the user back to the start of the loop
        else:
            print("Please enter a valid response (a %, a number above 0 or e.g. $500)")


all_cost = 200

profit_goal = profit_goal(all_cost)
print(profit_goal)

#
# for item in range (0, 6):
#     profit_target = profit_goal(all_costs)
#     print(f"Profit Target: ${profit_target:.2f}")
#     print(f"Total Sales: ${all_costs + profit_target:.2f}")
#     print()
