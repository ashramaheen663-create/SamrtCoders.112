#LOOPS:APPLIED LOOP PROBLEMS
#PRINT ALL FACTORS OF A NUMBER
num = int(input("ENTER A NUMBER:"))
print("FACTORS OF", num, "ARE:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)