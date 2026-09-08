#CONDITIONAL STATEMENTS
#CHECK IF YEAR IS LEAP YEAR OR NOT
year = int(input("Enter a year: "))
if year % 4 == 0:
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")