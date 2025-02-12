# Task 3: Fibonacci Sequence Generator 

Number = int(input("Enter the number of Fibonacci: "))

fib_sequence = [0, 1]

for i in range(2, Number):
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

for num in fib_sequence[:Number]:
    print(num)