#CONDITIONAL STATEMENTS
#CHECK IF A NUMBER IS POSITIVE,NEGATIVE,OR ZERO THEN IF POSITIVE CHECK EVEN OR ODD
a = int(input("Enter a number: "))
if a > 0:
	print("Positive")
	if a % 2 == 0:
		print("Even")
	else:
		print("Odd")
elif a < 0:
	print("Negative")
else:
	print("Zero")