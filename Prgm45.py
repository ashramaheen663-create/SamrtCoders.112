#LOOPS:BASIC COUNTING AND ITERATION
#PRINT ALL EVEN NUMBERS FROM 1 TO N
n = int(input("Enter a number: "))
print("Even numbers from 1 to", n, "are:")
for i in range(2, n + 1, 2):
    print(i)