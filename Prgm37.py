#CONDITIONAL STATEMENTS
#GIVEN COORDINATES(X,Y) DETERMINE WHICH QUADRANT THE POINT LIES IN 
X = float(input("Enter the x-coordinate: "))
Y = float(input("Enter the y-coordinate: "))
if X > 0 and Y > 0:
    print("The point lies in the first quadrant.")
elif X < 0 and Y > 0:
    print("The point lies in the second quadrant.")
elif X < 0 and Y < 0:
    print("The point lies in the third quadrant.")
elif X > 0 and Y < 0:
    print("The point lies in the fourth quadrant.")
else:
    print("The point lies on an axis.")