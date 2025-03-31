# Faith Green
# 03/31/25
# Assignment Name: Budget Calculation for Travel
# This program asks the user for their travel budget, destination, and expenses for gas, accommodation, and food,
# then calculates and displays the remaining budget after subtracting the expenses.

# Ask user to enter their budget
budget = float(input("Enter your total budget for the trip: $"))

# Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# Ask user for amount they will spend on gas
gas_expenses = float(input("Enter the amount you will spend on gas: $"))

# Ask user for amount they will spend on accommodation
accommodation_expenses = float(input("Enter the amount you will spend on accommodation: $"))

# Ask user for amount they will spend on food
food_expenses = float(input("Enter the amount you will spend on food: $"))

# Add expenses
total_expenses = gas_expenses + accommodation_expenses + food_expenses

# Subtract expenses from budget
remaining_budget = budget - total_expenses

# Display the results
print("\n----Budget Breakdown----")
print(f"Your travel destination: {destination}")
print(f"Total budget: ${budget:.2f}")
print(f"Gas expenses: ${gas_expenses:.2f}")
print(f"Accommodation expenses: ${accommodation_expenses:.2f}")
print(f"Food expenses: ${food_expenses:.2f}")
print(f"Total expenses: ${total_expenses:.2f}")
print(f"Remaining budget: ${remaining_budget:.2f}")
