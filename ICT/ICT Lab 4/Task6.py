# Task 6: Summation Of Numbers 

even = 0
odd = 0

for i in range(1, 101):
    if i % 2 == 0:
        even += i 
    else:
        odd += i 

print("Even =", even)
print("Odd =", odd)