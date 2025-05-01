# Faith Green
# 05/01/2025
# Assignment name: P5LAB
# This program calculates the most efficient number of dollars, quarters, dimes, nickels, and pennies
# based on the amount of money entered by the user using the previous assignment P3Lab

import random

# Function to calculate and display the number of coins and bills
def disperse_change(amount):
    # Convert the amount to an integer number of cents
    amount_in_cents = int(round(amount * 100))
    
    # Calculate the number of dollars
    dollars = amount_in_cents // 100
    amount_in_cents %= 100

    # Calculate the number of quarters
    quarters = amount_in_cents // 25
    amount_in_cents %= 25

    # Calculate the number of dimes
    dimes = amount_in_cents // 10
    amount_in_cents %= 10

    # Calculate the number of nickels
    nickels = amount_in_cents // 5
    amount_in_cents %= 5

    # The remaining amount is in pennies
    pennies = amount_in_cents

    # Display the results
    print("Change to be given:")
    if dollars > 0:
        print(f"{dollars} dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} penn{'ies' if pennies > 1 else 'y'}")

# Main function
def main():
    # Generate a random float value between 0.01 and 100.00, rounded to 2 decimal places
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    
    # Display the random amount owed to the store
    print(f"Amount owed: ${amount_owed:.2f}")
    
    # Get the amount of money from the user
    amount_paid = float(input("Enter amount paid: $"))

    # If the amount is less than the amount owed, inform the user
    if amount_paid < amount_owed:
        print("Insufficient payment. Please enter enough money.")
        return
    
    # Calculate and display the change
    change = amount_paid - amount_owed
    print(f"Total change: ${change:.2f}")
    
    # Call the function to dispense the change
    disperse_change(change)

# Call the main function to run the program
if __name__ == "__main__":
    main()
