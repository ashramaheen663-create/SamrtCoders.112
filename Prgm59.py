#loops:MATH THEORY
#FIND THE L.C.M OF TWO NUMBERS
num1 = int(input("ENTER THE FIRST NUMBER:"))
num2 = int(input("ENTER THE SECOND NUMBER:"))
if num1 > num2:
    greater = num1
else:
    greater = num2
while True:
    if greater % num1 == 0 and greater % num2 == 0:
        lcm = greater
        break
    greater += 1
print("L.C.M:", lcm)