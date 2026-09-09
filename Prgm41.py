#CONDITIONAL STATEMENTS
#CLOCK ANGLE: GIVEN HOURAND MINUTES, FIND THE ANGLE BETWEEN THE HOUR AND MINUTE HANDS OF A CLOCK
hour = int(input("Enter the hour: "))
minutes = int(input("Enter the minutes: "))
angle = abs(30 * hour - 5.5 * minutes)
print("The angle between the hour and minute hands is:", angle)