#CONDITIONAL STATEMENTS
# ATM WITHDRAWL :APPROVE OR REJECT A WITHDRAWL BASED ON AMOUNT,BALANCE,AND MINIMUM-BALANCE ISSUES
amount = float(input("Enter the withdrawal amount: "))
balance = float(input("Enter your current balance: "))
if amount > balance:
    print("Withdrawal rejected: Insufficient funds.")
elif balance - amount < 100:
    print("Withdrawal rejected: Minimum balance requirement not met.")
else:
    print("Withdrawal approved.")