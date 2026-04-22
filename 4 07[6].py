gpa = float(input("Enter GPA: "))
income = int(input("Enter family income: "))

if gpa >= 3.5 and income < 30000:
    print("Full scholarship")
elif gpa >= 3.0 and income < 50000:
    print("Partial scholarship")
else:
    print("No scholarship")
