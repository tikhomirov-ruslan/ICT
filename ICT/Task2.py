# 1
password1 = input()
password2 = input()

if password1 == password2:
    print("Password accepted")
else:
    print("Password not accepted")

print()

# 2
a = int(input())
if a // 2 == 0:
    print("Even value")
else:
    print("Odd number")

print()

# 3
a = int(input())
b = int(input())

if a > b:
    print(a)
else:
    print(b)

print()

# 4
age = int(input())

if age <= 13:
    print("Childhood")
elif age >= 14 and age <= 24:
    print("youth")
elif age >= 25 and age <= 59:
    print("maturity")
else:
    print("old age")

print()

# 5
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    type = "Equilateral"
elif a == b or a == c or b == c:
    type = "Isosceles"
else:
    type = "Versatile"

print(type)

print()

