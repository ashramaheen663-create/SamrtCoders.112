a=int(input("Enter your Age: "))
if a<=12:
    print("Ticket not applicable.")
elif a<=19:
    print("Ticket Amount is RS-100.")
elif a<=59:
    print("Ticket Amount is RS-200.")
else:
    print("Ticket Amount is RS-150.")