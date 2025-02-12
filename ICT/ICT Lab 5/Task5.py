# Task 5: Prime Number Checker 

num = int(input("Enter the number: "))

isPrime = True

if num <= 1:
    print("The number must be more than 1")
else: 
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            isPrime = False

    if isPrime == False:
        print("The number is not prime")

    elif isPrime == True:
        print("The number is prime")
