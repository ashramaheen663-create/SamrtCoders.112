#LOOPS: SERIES AND PATTERNS
#COMPUTE THE SUM 1+1/2+1/3+1/4+...+1/N
n=int(input("ENTER THE Nth number:"))
total = 0
for i in range(1, n + 1):
	total += 1 / i
print("Sum:", total)