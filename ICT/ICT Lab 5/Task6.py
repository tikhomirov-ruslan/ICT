# Task 6: Simple Text-Based Menu 

while True:
    print("Menu Display: ")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
        
    choice = input("Choose the Variant (1-5): ")

    operation = ['+', '-', '*', '/']

    if choice == "1":
        operation == "+"
        a = int(input("a = "))
        b = int(input("b = "))
        print(a + b)
        print()

    elif choice == "2":
        operation == "-"
        a = int(input("a = "))
        b = int(input("b = "))
        print(a - b)
        print()

    elif choice == "3":
        operation == "*"
        a = int(input("a = "))
        b = int(input("b = "))
        print(a * b)
        print()

    elif choice == "4":
        operation == "/"
        a = int(input("a = "))
        b = int(input("b = "))

        if b != 0:
            print(a // b)
            print()
            
        else:
            print("Error: Division by zero")
            print()


    elif choice == "5":
        print("Exit")
        break

    else:
        print("Error! Print only the number (1-5).")


    # a = int(input("a = "))
    # b = int(input("b = "))

    # if choice == "1":
    #     print(a + b)
    #     print()

    # elif operation == '-' and choice == "2":
    #     print(a - b)
    #     print()

    # elif operation == '*' and choice == "3":
    #     print(a * b)
    #     print()

    # elif operation == '/' and choice == "4":
    #     if b != 0:
    #         print(a // b)
    #     else:
    #         print("Error: Division by zero")

    # elif operation == 'q':
    #     break

    # else:
    #     print("Error: Operation is not found")