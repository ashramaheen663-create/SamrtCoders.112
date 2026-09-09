#CONDITIONAL STATEMENTS
#READ THE COST PRICE AND SELLING PRICE PRINT PROFIT,LOSS OR NO PROFIT NO LOSS
CP = float(input("Enter the cost price: "))
SP= float(input("Enter the selling price: "))
if SP > CP:
    print("Profit")
elif SP < CP:
    print("Loss")
else:
    print("No Profit No Loss")