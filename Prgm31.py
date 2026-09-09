#CONDITIONAL STATEMENTS
#READ MONTH NUMBER(1_12) FROM USER AND PRINT NUMBER OF DAYS IN THAT MONTH.
month=int(input("Enter the month number (1-12): "))
YEAR = int(input("Enter the year: "))
if month in (1, 3, 5, 7, 8, 10, 12):
    print("The number of days in the month is: 31")
elif month in (4, 6, 9, 11):
    print("The number of days in the month is: 30")
elif month == 2 and YEAR%4 == 0:
    print("The number of days in the month is: 29")
elif month == 2 and YEAR%4 != 0:
    print("The number of days in the month is: 28")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")