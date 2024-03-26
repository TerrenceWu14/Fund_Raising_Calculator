import re


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


# calculates the profit goal
def profit_goal():
    while True:
        # asks the user for the profit goal
        response = input("Profit Goal? ")

        # the allowed string pattern (allows only integers above 0
        # with $ at the start or %$ at the end)
        allowed = r'^[$]?[1-9]\d*(?:\.\d+)?[%$]?$'

        # if the response matches the allowed pattern, returns response
        if re.match(allowed, response):
            print("Thanks")
            return ""

        # else sends the user back to the start of the loop
        else:
            print("Please enter a valid response (a %, a number above 0 or e.g. $500)")


all_cost = 200

profit_goal = profit_goal()
print(profit_goal)

#
# for item in range (0, 6):
#     profit_target = profit_goal(all_costs)
#     print(f"Profit Target: ${profit_target:.2f}")
#     print(f"Total Sales: ${all_costs + profit_target:.2f}")
#     print()
