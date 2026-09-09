#LOOPS:SERIES AND PATTERNS
#FIBBONACI SERIES UPTO N TERMS
n=int(input("ENTER THE Nth number:"))
a=0
b=1
print(a, b, end=" ")
for _ in range(2, n):
	c=a+b
	print(c, end=" ")
	a=b
	b=c