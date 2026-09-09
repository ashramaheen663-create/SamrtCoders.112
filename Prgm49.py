#LOOPS:DIGIT BASED PRBLMS
#FIND THE SUM OF DIGITS OF A NUMBER
n=int(input("Enter a number:"))
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
print("The sum of the digits of the number is:", sum)