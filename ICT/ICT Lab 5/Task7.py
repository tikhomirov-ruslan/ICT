# Task 7: BMI Calculator Using Conditional Operators  
def bmi_calculator():
    try:
        weight = float(input("Enter your weight: "))
        height = float(input("Enter your height: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers!")
            return
            
    except ValueError:
        print("Error! Only Numbers!")
        return

 
    bmi = (weight / (height ** 2))

 
    if bmi < 18.5:
        category = "Underweight (< 18.5)"
    elif 18.5 <= bmi < 25:
        category = "Normal weight(18.5 - 24.9)"
    elif 25 <= bmi < 30:
        category = "Overweight (25 - 29.9)"
    else:
        category = "Obesity (30 and above)"

    print(f"IMT: {bmi:.2f}")
    print(f"Category: {category}")

bmi_calculator()