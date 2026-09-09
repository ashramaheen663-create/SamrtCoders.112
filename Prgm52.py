#LOOPS:DIGIT BASED PRBLMS
#HAPPY NUMBER
n=int(input("Enter a number:"))
while n>9:
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit**2
        n=n//10
    n=sum
if n==1:
    print("Happy number:", n)
else:
    print("Not a happy number:", n)
