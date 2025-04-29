# Faith Green
# April 29, 2025
# P4HW2 – Employee Salary Calculation with Overtime
# This program calculates the gross pay, regular pay, overtime pay, and hours worked for multiple employees
# based on user input and displays total regular pay, overtime pay, gross pay, and employee count.

# Initialize totals and employee count
total_regular_pay = 0
total_overtime_pay = 0
total_gross_pay = 0
employee_count = 0

# Loop to input multiple employee data
while True:
    # Ask for employee name
    employee_name = input("Enter employee's name (or type 'Done' to finish): ")
    
    # If the user enters 'Done', terminate the program
    if employee_name.lower() == 'done':
        break
    
    # Ask for pay rate and hours worked
    try:
        pay_rate = float(input(f"Enter {employee_name}'s pay rate (per hour): $"))
        hours_worked = float(input(f"Enter {employee_name}'s hours worked: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for pay rate and hours worked.")
        continue
    
    # Calculate regular pay and overtime pay
    if hours_worked > 40:
        regular_pay = 40 * pay_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
    else:
        regular_pay = hours_worked * pay_rate
        overtime_hours = 0
        overtime_pay = 0
    
    # Calculate gross pay
    gross_pay = regular_pay + overtime_pay
    
    # Update totals
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    employee_count += 1
    
    # Display detailed information for each employee
    print(f"\n--- {employee_name}'s Pay Details ---")
    print(f"Hours worked: {hours_worked}")
    print(f"Pay rate: ${pay_rate:.2f}")
    print(f"Overtime hours: {overtime_hours}")
    print(f"Overtime pay: ${overtime_pay:.2f}")
    print(f"Regular pay: ${regular_pay:.2f}")
    print(f"Gross pay: ${gross_pay:.2f}")
    print("-------------------------------")

# After exiting the loop, display results
print("\n---------- Results ----------")
print(f"Number of employees entered: {employee_count}")
print(f"Total regular pay for all employees: ${total_regular_pay:.2f}")
print(f"Total overtime pay for all employees: ${total_overtime_pay:.2f}")
print(f"Total gross pay for all employees: ${total_gross_pay:.2f}")
print("-----------------------------")
