#LOOPS:APPLIED PROBLEMS
#FIND THE SUM OF EVEN AND ODD NUMBERS BETWEEN 1 TO N SEPARATELY
n = int(input("ENTER THE Nth NUMBER:"))
even_sum = 0
odd_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("SUM OF EVEN NUMBERS:", even_sum)
print("SUM OF ODD NUMBERS:", odd_sum)