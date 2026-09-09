#loops:MATH THEORY
#FIND THE G.C.D OF TWO NUMBERS
num1 = int(input("ENTER THE FIRST NUMBER:"))
num2 = int(input("ENTER THE SECOND NUMBER:"))
if num1 < num2:
    smaller = num1
else:
    smaller = num2
for i in range(1, smaller + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
print("G.C.D:", gcd)