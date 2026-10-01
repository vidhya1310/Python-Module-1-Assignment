food_order = {"Pizza": 2, "Burger": 1, "Fries": 3 , "Waffle" : 4}

# All food items
print("Food Items:", food_order.keys())

# All quantities
print("Quantities:", food_order.values())

# Food item with quantity
print("Food and Quantity:")

for item, quantity in food_order.items():
    print(item, ":", quantity)