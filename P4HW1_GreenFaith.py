# Faith Green
# April 29, 2025
# P4HW1 – Score Processing with Validation and Grading
# This program collects a user-defined number of scores, validates them,
# calculates the average after dropping the lowest score,
# and displays the letter grade based on the average.

# Ask how many scores the user wants to enter
num_scores = int(input("How many scores would you like to enter? "))

scores = []

# Loop to collect valid scores
for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score #{i + 1}: "))
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Drop the lowest score
lowest = min(scores)
scores.remove(lowest)

# Calculate average of remaining scores
average = sum(scores) / len(scores)

# Determine letter grade
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display results
print("\n---------- Results ----------")
print(f"Lowest score dropped: {lowest}")
print(f"Scores remaining: {scores}")
print(f"Average score: {average:.2f}")
print(f"Letter grade: {grade}")
print("-----------------------------")
