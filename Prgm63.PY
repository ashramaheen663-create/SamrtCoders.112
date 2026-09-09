#LOOPS:SERIES & PATTERNS
#FIND X^N USING FOR LOOP
x=int(input("ENTER THE VALUE OF X:"))
n=int(input("ENTER THE VALUE OF N:"))
result=1
for i in range(n):
    result*=x
print("X^N =", result)