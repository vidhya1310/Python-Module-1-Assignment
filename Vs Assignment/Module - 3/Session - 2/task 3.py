# Create orders.txt
file = open("orders.txt", "w")

file.write("Pizza\n")
file.write("Burger\n")
file.write("Sandwich\n")
file.write("Pasta\n")
file.write("Biryani\n")

file.close()

# Read orders one by one
file = open("orders.txt", "r")

while True:
    order = file.readline()

    if not order:
        break

    print("Order:", order.strip())
    print("File pointer position:", file.tell())

file.close()