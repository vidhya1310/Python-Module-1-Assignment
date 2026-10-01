def update_cart(cart, item, qty): 

    cart.update({item: qty}) 
    return cart 

cart = { "Laptop": 1, "Mouse": 2 , "Headphone" :3 } 

cart = update_cart(cart, "Keyboard", 1) 
print("Updated Cart:", cart)