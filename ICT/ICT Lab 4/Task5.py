# Task 5: Combining Food 

from itertools import product

bread = ["white bread", "black bread"]
meat = ["ham", "beef", "chicken"]
vegetables = ["tomato", "cucumber", "onion"]
sauces = ["mayonnaise", "ketchup"]

sandwich_combinations = list(product(bread, meat, vegetables, sauces))

for combo in sandwich_combinations:
    print(f"Bread: {combo[0]}, Meat: {combo[1]}, Vegetable: {combo[2]}, Sauce: {combo[3]}")