#LOOPS:BASIC COUNTING AND ITERATION
#PRINT ALL ODD NUMBERS FROM 1 TO N
n=int(input("Enter a number:"))
for i in range(1,n+1):
    if i%2!=0:
        print(i)