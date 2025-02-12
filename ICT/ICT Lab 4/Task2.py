# Task 2: Calculator using a loop 

while True:

    operation = input("Operation (+, -, *, /): ")

    if operation in ['+', '-', '*', '/']:
        a = int(input("a = "))
        b = int(input("b = "))

        if operation == '+':
            print(a + b)
        elif operation == '-':
            print(a - b)
        elif operation == '*':
            print(a * b)
        elif operation == '/':
            if b != 0:
                print(a // b)
            else:
                print("Error: Division by zero")

    elif operation == 'q':
        break

    else:
        print("Error: Operation is not found")
    