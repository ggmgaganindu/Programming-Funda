income = float(input("Enter income: "))

if income >= 100000:
    tax = income * 0.20
elif 50000 <= income < 100000:
    tax = income * 0.10
else:
    tax = 0

print("Tax:", tax)
