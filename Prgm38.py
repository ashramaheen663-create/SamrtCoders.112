#CONDITIONAL STATEMENTS
#CHECK IF A THREE DIGIT NUMBER IS ARMSTRONG OR NOT
num = int(input("Enter a three-digit number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")