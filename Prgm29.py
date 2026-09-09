#CONDITIONAL STATEMENTS
#29	Given 3 sides, check if a valid triangle can be formed
a = int(input("Enter the length of side 1: "))
b = int(input("Enter the length of side 2: "))
c = int(input("Enter the length of side 3: "))
if a + b > c and b + c > a and c + a > b:
    print("A triangle can be formed with the given sides.")
else:
    print("A triangle cannot be formed with the given sides.")
