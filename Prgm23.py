t=int(input("Enter the hour in 24-hour format: "))
if t<=12:
    print("Good Morning")
elif t<=16:
    print ("Good Afternoon")
elif t<=20:
    print ("Good Evening")
else:
    print ("Good Night")    