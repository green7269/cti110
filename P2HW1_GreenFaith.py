# Faith Green
# 04/09/25
# Assignment Name: Travel Budget Calculator
# A brief description of the project: This program calculates and displays a travel budget breakdown, including costs for 
# destination, gas, accommodation, and food. The user inputs the cost data, and the output is neatly formatted with money values.

# List of destinations
destinations = ["Paris", "London", "Tokyo", "New York", "Sydney"]

# Print header
print(f"{'Destination':<20}{'Gas ($)':>12}{'Accommodation ($)':>18}{'Food ($)':>12}{'Total ($)':>12}")

# Loop through each destination, prompt for input, and calculate the total cost
for destination in destinations:
    # Prompt user for gas, accommodation, and food costs (convert to float)
    gas = float(input(f"Enter the gas cost for traveling to {destination} ($): "))
    accommodation = float(input(f"Enter the accommodation cost for {destination} ($): "))
    food = float(input(f"Enter the food cost for {destination} ($): "))

   # Calculate total cost for the destination
    total_cost = gas + accommodation + food
    
    # Print the results, formatted with dollar signs and two decimal places
    print(f"{destination:<20}${gas:>11.2f}${accommodation:>17.2f}${food:>12.2f}${total_cost:>12.2f}")
