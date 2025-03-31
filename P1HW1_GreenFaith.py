# Faith Green
# 03/31/25
# P1HW1
# Using math expressions with user input

print("-------Calulating Exponents-------")

print()
print()

#get integer from the string
base_value = int (input("Enter an integer as the base value: "))
exponent = int (input("Enter an interger as the exponent: "))

print()
print()

# Display math result to the user
print(base_value, "raised to the power of", exponent, "is", base_value**exponent, "!!")

print()
print()

#Addition and Subtraction Section
print("-------Addition and Subtraction-------")
print()
print()

#Enter a starting integer
starting = int (input("Enter a starting integer:  "))

#Enter an integer to add
add = int (input("Enter an integer to add:  "))

#Enter an integer to subtract
subtract = int (input("Enter an integer to subtract:  "))

print()
print()

#Display math result to user
print(starting, "+", add, "-", subtract, "is equal to", starting + add - subtract)
