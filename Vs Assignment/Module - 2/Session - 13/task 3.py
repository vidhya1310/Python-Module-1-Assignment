names = ['Shoes', 'Bag', 'Watch', 'Headphones']
prices = [999, 1500, 700, 2200]

products = [(names[i], prices[i]) for i in range(len(names)) if prices[i] > 1000]

print(products)