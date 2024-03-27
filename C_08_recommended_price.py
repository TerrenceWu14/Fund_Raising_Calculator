import math


# rounding function
def round_up(amount, var_round_to):
    return int(math.ceil(amount / var_round_to)) * var_round_to


how_many = 5
total = 3
profit_goal = 10
round_to = 2

sales_needed = total + profit_goal

print(f"Total: {total}")
print(f"Profit Goal: ${profit_goal:.2f}")

selling_price = sales_needed / how_many
print(f"Selling Price (not rounded): ${selling_price:.2f}")

recommended_price = round_up(selling_price, round_to)
print(f"Recommended Price: ${recommended_price:.2f}")
