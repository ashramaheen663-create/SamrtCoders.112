#CONDITIONAL STATEMENTS
#Read a number (1–7) and print the corresponding day of the week	Resource Link

day = int(input("Enter DAY number (1-7): "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid input. Please enter a number between 1 and 7.")