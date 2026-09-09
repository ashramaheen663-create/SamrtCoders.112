#LOOPS:DIGIT BASED PRBLMS
#EXTRACT AND PRINT EACH DIGIT OF A NUMBER
n=int(input("Enter a number:"))
while n>0:
    digit=n%10
    print(digit)
    n=n//10