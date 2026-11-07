class ZomatoOrder:
    def add_item(self, item_name, quantity=1):
        print("Item:", item_name)
        print("Quantity:", quantity)


order = ZomatoOrder()

order.add_item("Pizza", 2)
print()

order.add_item("Burger", 3)