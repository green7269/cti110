# Faith Green
# 04/09/25
# Assignment Name: Vehicle MPG Calculator
# A brief description of the project: This program creates a dictionary with vehicle names and MPG values.
# It prompts the user to select a vehicle, and calculates the gallons of gas needed to drive a specified distance.

# Create a dictionary with vehicle names as keys and their MPG values as values
vehicle_mpg = {  "Camaro": 18.21,   "Prius": 52.36, "Model S": 110,  "Silverado": 26}

# Get all the keys from the dictionary
keys = vehicle_mpg.keys()

# Print the keys
print("Available vehicles:", keys)

# Prompt the user to enter a vehicle name from the dictionary
vehicle = input("Enter the vehicle name from the list: ")

# Check if the vehicle is in the dictionary
if vehicle in vehicle_mpg:
    mpg = vehicle_mpg[vehicle]
    print(f"The MPG for {vehicle} is {mpg:.2f}.")
    
    # Prompt the user to enter the number of miles they will drive
    miles = float(input(f"Enter the number of miles you will drive the {vehicle}: "))
    
    # Calculate the gallons of gas needed
    gallons_needed = miles / mpg
    
    # Display the gallons of gas needed, rounded to two decimal places
    print(f"You will need {gallons_needed:.2f} gallons of gas to drive {miles} miles in the {vehicle}.")

