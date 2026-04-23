i = 0
while i <= 10:
    print(i)
    i += 1

    
i = 10
while i >= 0:
    print(i)
    i -= 1

i = 1
total = 0

while i <= 10:
    total += i
    i += 1

print("Sum:", total)

i = 1
while i <= 10:
    print("5 x", i, "=", 5 * i)
    i += 1
    count = 1
total = 0

while count <= 5:
    num = int(input("Enter number: "))
    total += num
    count += 1

print("Total:", total)
count = 1
total = 0

while count <= 10:
    mark = float(input("Enter mark: "))
    total += mark
    count += 1

average = total / 10

print("Total:", total)
print("Average:", average)

if average < 50:
    print("Fail")
else:
    print("Pass")
