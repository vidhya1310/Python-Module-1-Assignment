
restaurants = ['Burger Hub', 'Pizza Point', 'Sushi House']

delivery_times = [30, 25, 40]

for restaurant, time in zip(restaurants, delivery_times):
    print(restaurant, "-", time, "min")

