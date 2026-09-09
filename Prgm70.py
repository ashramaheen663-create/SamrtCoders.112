#LOOPS: APPLIED PROBLEMS
#CHECK IF A NUMBER IS PERFECT NUMBER OR NOT
num = int(input("ENTER A NUMBER:"))
divisors_sum = 0
for i in range(1, num):
    if num % i == 0:
        divisors_sum += i
if divisors_sum == num:
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")