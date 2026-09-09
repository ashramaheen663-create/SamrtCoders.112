#LOOPS:APPLIED PROBLEMS
#CHECK IF A NUMBER IS AMSTRONG(GENRALIZED FOR ANY DIGITS)
num = int(input("ENTER A NUMBER:"))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")