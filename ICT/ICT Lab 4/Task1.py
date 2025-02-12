# Task 1: Calculator using conditional operators 

a = int(input())
b = int(input())

sum = str(a + b)
difference = str(a - b)
product = str(a * b)

if b != 0:
    division = str(a // b)
    a = str(a)
    b = str(b)
    print(a + " / " + b + " = " + division)
else:
    print("Error: Division by zero")

a = str(a)
b = str(b)

print(a + " + " + b + " = " + sum)
print(a + " - " + b + " = " + difference)
print(a + " * " + b + " = " + product)