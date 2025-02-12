# 1
n = int(input())

if 1 <= n <= 20:
    for _ in range(n):
        print('*' * 19)

print()

# 2
word = input()

for i in range(10):
    print(f"{i} {word}")

print()

# 3
n = int(input())

if n >= 2:
    for i in range(n, 0, -1):
        print('*' * i)

print()

# 4
m = int(input())
n = int(input())

for num in range(m, n):
    print(num)

print()

# 5
m = int(input())
n = int(input())

if m < n:
    for num in range(m, n + 1):
        print(num)
else:
    for num in range(m, n - 1, -1):
        print(num)

print()

# 6
m = int(input())
n = int(input())

for num in range(m, n - 1, -1):
    if num % 2 != 0:
        print(num)