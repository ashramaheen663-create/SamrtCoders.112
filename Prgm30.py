#CONDITIONAL STATEMENTS
#30	Build a simple calculator (+, −, ×, ÷) using switch-case
A=int(input("Enter first number: "))
B=int(input("Enter second number: "))
C=input("Enter the operator (+, -, *, /): ")
if C=='+':
    print("The result of addition is:", A+B)
elif C=='-':
    print("The result of subtraction is:", A-B)
elif C in ('*'):
    print("The result of multiplication is:", A*B)
elif C in ('/'):
    print("The result of division is:", A/B)