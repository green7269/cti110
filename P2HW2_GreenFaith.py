# Faith Green
# 04/09/25
# Assignment Name: P2HW2
# Brief description of program: This program asks the user to enter grades for six modules, stores them in a list,
# and displays the lowest grade, highest grade, sum of grades, and the average grade.

# List to store grades entered by the user
grades = []

# Prompting user to enter grades for each module
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

# Calculating required values
lowest_grade = min(grades)  # Finding the lowest grade
highest_grade = max(grades)  # Finding the highest grade
total_sum = sum(grades)  # Finding the sum of all grades
average_grade = total_sum / len(grades)  # Finding the average of grades

# Displaying the results
print(f"The lowest grade is: {lowest_grade}")
print(f"The highest grade is: {highest_grade}")
print(f"The sum of the grades is: {total_sum}")
print(f"The average of the grades is: {average_grade:.2f}")


