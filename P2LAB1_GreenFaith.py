# Faith Green
# 04/09/25
# Assignment Name: Circle Calculations
# A brief description of the project: This program calculates the diameter, circumference, and area of a circle
# given the radius input by the user, and formats the output accordingly.

import math

# Get user input for the radius (float)
radius = float(input("Enter the radius of the circle: "))

# Calculate the diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius**2

# Display the results with the specified formatting
print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")
