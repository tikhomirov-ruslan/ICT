# Task 10: List Comprehensions and Filtering  

numbers = list(range(1, 51))

filtered_numbers = [num for num in numbers if num % 3 == 0 and num % 5 == 0]

print("The numbers that are divisible by both 3 and 5: ", filtered_numbers)
