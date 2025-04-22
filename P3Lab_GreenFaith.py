# Faith Green
# 04/22/25
# Assignment name: P3LAB
#This program calculates the most efficient number of dollars, quarters, dimes, nickels, and pennies
# based on the amount of money entered by the user.

# Function to calculate the number of coins and bills
def calculate_change(amount):
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

    # Return the results
    return dollars, quarters, dimes, nickels, pennies

# Function to display the result
def display_result(dollars, quarters, dimes, nickels, pennies):
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
    # Get the amount of money from the user
    amount = float(input("Enter an amount of money (e.g., 5.67): $"))

    #If the amount is 0.00, print "No change needed" and exit
    if amount == 0.00:
        print("No change.")
        return
    
    # Call the function to calculate the change
    dollars, quarters, dimes, nickels, pennies = calculate_change(amount)
    
    # Call the function to display the result
    display_result(dollars, quarters, dimes, nickels, pennies)

# Call the main function to run the program
if __name__ == "__main__":
    main()
