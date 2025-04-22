# Faith Green
# 04/22/2025
# Assignment Name: P3HW2 - Salary Calculator with Overtime
# Description: This program calculates the gross pay for an employee based on their weekly hours worked 
# and hourly pay rate, including overtime for any hours worked beyond 40 hours.

# Get employee details
employee_name = input("Enter the employee's name: ")
hours_worked = float(input("Enter the number of hours worked this week: "))
pay_rate = float(input("Enter the employee's pay rate: $"))

# Initialize overtime variables
overtime_hours = 0
overtime_pay = 0

# Check for overtime (more than 40 hours)
if hours_worked > 40:
    overtime_hours = hours_worked - 40  # Calculate overtime hours
    overtime_rate = pay_rate * 1.5  # Overtime is paid at 1.5 times the normal pay rate
    overtime_pay = overtime_hours * overtime_rate  # Calculate overtime pay

# Calculate regular pay
regular_hours = min(hours_worked, 40)  # Regular hours are up to 40
regular_pay = regular_hours * pay_rate  # Calculate regular pay

# Calculate total gross pay
gross_pay = regular_pay + overtime_pay  # Total pay includes regular pay and overtime pay

# Display the results
print("\nEmployee Information:")
print(f"Employee Name: {employee_name}")
print(f"Pay Rate: ${pay_rate:.2f}")
print(f"Hours Worked: {hours_worked} hours")
print(f"Regular Hours Worked: {regular_hours} hours")
print(f"Overtime Hours: {overtime_hours} hours")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Regular Pay: ${regular_pay:.2f}")
print(f"Gross Pay: ${gross_pay:.2f}")

