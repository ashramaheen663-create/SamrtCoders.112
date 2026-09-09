#LOOPS:SERIES & PATTERNS
# COMPUTE: 1!+2!+3!+4!+...+N!
n=int(input("ENTER THE Nth number:"))
sum = 0
for i in range(1, n + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    sum += factorial
print("THE SUM OF FACTORIALS IS:", sum)