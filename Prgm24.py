#CONDITIONAL STATEMENTS
#Login Validator : Check whether a username and password combination is valid.
username = input("Enter username: ")
password = input("Enter password: ")
#USING PREDEFINED USERNAME AND PASSWORD
if username == "admin" and password == "pass1256":
    print("Login successful.")
else:
    print("Invalid username or password.")