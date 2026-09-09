#LOOPS:SERIES AND PATTERNS
#COMPUTE: 1-2+3-4+5... upto N terms
n=int(input("ENTER THE Nth number:"))
total = 0
for i in range(1, n + 1):
	if i % 2 == 0:
		total -= i
	else:
		total += i
print("Sum:", total)