#CONDITIONAL STATEMENTS
#Check if a triangle is equilateral, isosceles, or scalene given 3 sides
a = int(input("Enter the length of side 1: "))
b = int(input("Enter the length of side 2: "))
c = int(input("Enter the length of side 3: "))
if a == b == c:
    print("The triangle is equilateral.")
elif a == b or b == c or c == a:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")