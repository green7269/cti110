# Multiplication table program with for and while loops

run_again = "yes"

while run_again.lower() == "yes":
    # Ask the user for an integer
    number = int(input("Enter an integer: "))
    
    if number >= 0:
        print(f"\nMultiplication table for {number}:")
        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")
    else:
        print("Sorry, this program does not handle negative numbers.")

    # Ask the user if they want to run the program again
    run_again = input("\nDo you want to run the program again? (yes or no): ")

print("Exiting Program ...")
