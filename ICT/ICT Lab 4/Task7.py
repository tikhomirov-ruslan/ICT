# Task 7: The Factorial Of The Number 

n = int(input())

if n == 0 or n == 1:
    print(1)
elif n >= 2: 
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(result)
else:
    print("Error: Factorial can not be negative")

