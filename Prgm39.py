#CONDITIONAL STATEMENTS
#GIVEN HOURS WORKED AND RATE, COMPUTE SALARY WITH OVERTIME(>40HRS AT 1.5X RATE)
hours_worked = float(input("Enter the hours worked: "))
rate = float(input("Enter the rate: "))
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    salary = (40 * rate) + (overtime_hours * rate * 1.5)
else:
    salary = hours_worked * rate
print("The salary is:", salary)