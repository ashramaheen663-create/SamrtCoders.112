#CONDITIONAL STATEMENTS
#Given marks (0–100), print grade: A (≥90), B (≥80), C (≥70), D (≥60), F (<60)
m=int(input("Enter your marks : "))
if m>=90:
    print("Grade: A")
elif m>=80:
    print("Grade: B")
elif m>=70:
    print("Grade: C")
elif m>=60:
    print("Grade: D")
else:
    print("Grade: F")