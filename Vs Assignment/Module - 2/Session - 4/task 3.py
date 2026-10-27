order = ('Burger', 'Fries', 'Coke')
order_list = list(order)
order_list.append('Ice Cream')
order = tuple(order_list)

print("Final Order:", order)
