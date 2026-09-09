#LOOPS: APPLIED PROBLEMS
#CONVERT DECIMAL TO BINARY
import math

print("Performing program 71")
num = float(input("ENTER A DECIMAL NUMBER:"))
binary = ""
temp = num
while temp > 0:
    binary = str(temp % 2) + binary
    temp //= 2
print("BINARY OF", num, "IS:", binary)
print("Performing Program 72")
#CONVERT BINARY TO DECIMAL
binary_num = input("ENTER A BINARY NUMBER:")
decimal = 0
power = 0
for digit in reversed(binary_num):
    decimal += int(digit) * (2 ** power)
    power += 1
print("DECIMAL OF", binary_num, "IS:", decimal)
print("Performing program 73")
#READ NUMBERS UNTIL USER ENTERS -1 PRINT THE COUNT AND AVERAGE
count = 0
total = 0
while True:
    num = int(input("ENTER A NUMBER (-1 TO STOP):"))
    if num == -1:
        break
    count += 1
    total += num

if count > 0:
    average = total / count
    print("COUNT:", count)
    print("AVERAGE:", average)
else:
    print("NO NUMBERS ENTERED.")
print("Performing program 74")
#FIND THE SUM OF SERIES X-X^3/3!+X^5/5!-X^7/7!+...(SIN SERIES)
x = float(input("ENTER THE VALUE OF X:"))
n = int(input("ENTER THE NUMBER OF TERMS:"))
sum_series = 0
for i in range(n):
    term = ((-1) ** i) * (x ** (2 * i + 1)) / (math.factorial(2 * i + 1))
    sum_series += term
print("SUM OF SERIES:", sum_series)
print("Performing program 75")
#CHECK WHETHER A STRING IS PALINDROME OR NOT
text = input("ENTER A STRING:")
if text == text[::-1]:
    print("THE STRING IS A PALINDROME.")
else:
    print("THE STRING IS NOT A PALINDROME.")