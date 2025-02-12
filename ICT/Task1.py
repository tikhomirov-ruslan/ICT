# 1
list = [4, 8, 15, 16, 23, 42]
map = ' '.join(map(str, list))
print(map)

print()

# 2
for i in list:
    print(i)

print()

# 3
i = 0
n = int(input())

for i in range(1, n+1):
    print('*' * i)

print()

# 4
number = int(input())

print(number)
print(number + 1)
print(number + 2)

print()

# 5
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

print()

# 6
side = int(input())

volume = str(pow(side, 3))
surfaceArea = str(6 * pow(side, 2))

print("Объем = " + volume)
print("Площадь полной поверхности = " + surfaceArea)

print()

# 7
number = int(input())
a = str(number + 1)
b = str(number - 1)
c = str(number)

print("Следующее за числом " + c + " число: " + a)
print("Для числа " + c + " предыдущее число: " + b)  

print()

# 8
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(3 * (a + b + c + d))

print()

# 9
a = int(input())
b = int(input())

sum = str(a + b)
difference = str(a - b)
product = str(a * b)
a = str(a)
b = str(b)

print(a + " + " + b + " = " + sum)
print(a + " - " + b + " = " + difference)
print(a + " * " + b + " = " + product)

print()

# 10
sm = int(input())

meters = sm // 100

print(meters)