#CONDITIONAL STATEMENTS
#SCHOLARSHIP ELIGIBILITY DETERMINE ELIGIBILITY BASED ON MARKS,ATTENDANCE AND FAMILY INCOME
marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance percentage: "))
family_income = int(input("Enter your family income: "))
if marks >= 85 and attendance >= 75 and family_income <= 50000:
    print("You are eligible for the scholarship.")
else:
    print("You are not eligible for the scholarship.")