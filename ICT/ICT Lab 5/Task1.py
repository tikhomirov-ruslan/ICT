# Task 1: Temperature Converter Using Conditional Operators 

Temperature = input()

if Temperature == "C":
    Celsius = int(input("Enter temperature in Celsius: "))
    Fahrenheit = (Celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", Fahrenheit)

elif Temperature == "F":
    Fahrenheit = int(input("Enter temperature in Fahrenheit: "))
    Celsius = (Fahrenheit - 32) * 5/9
    print("Temperature in Celsius:", Celsius)

else:
    print("Invalid input. Please enter either 'C' for Celsius or 'F' for Fahrenheit.")