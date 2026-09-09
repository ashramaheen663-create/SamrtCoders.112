#CONDITIONAL STATEMENTS
#FIND THE ROOTS OF A QUADRATIC EQUATION
import math
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = b**2 - 4*a*c
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("The roots are real and different:")
    print("Root 1 =", root1)
    print("Root 2 =", root2)
elif d == 0:
    root = -b / (2*a)
    print("The root is real and repeated:")
    print("Root =", root)
else:
    print("The roots are complex and different.")