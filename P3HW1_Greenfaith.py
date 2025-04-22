# Faith Green
# 04/22/2025 
# This program takes a number grade, determines the average, and displays the letter grade for the average.
# Enter grades for six modules

# Prompt the user to input grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average for grades
low = min(grades)  # Finding the lowest grade
high = max(grades)  # Finding the highest grade
total_sum = sum(grades)  # Finding the sum of all grades
avg = total_sum / len(grades)  # Finding the average of grades

# Display the results
print(f"Lowest grade: {low}")
print(f"Highest grade: {high}")
print(f"Sum of grades: {total_sum}")
print(f"Average grade: {avg:.2f}")

# Determine letter grade for the average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')
