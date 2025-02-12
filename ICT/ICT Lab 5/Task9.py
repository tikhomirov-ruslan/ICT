# Task 9: Multiplication Table Generator  

def multiplication_table_generator():

    try:
        number = int(input("Enter the positive number: "))
        if number <= 0:
            print("The number must be positive and more than zero!")
            return
    except ValueError:
        print("Error! The number must be positive and more than zero!")
        return

    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

multiplication_table_generator()