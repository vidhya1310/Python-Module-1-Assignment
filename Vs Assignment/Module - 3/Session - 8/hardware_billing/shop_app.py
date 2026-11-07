
# Import style 1
import hardware_shop.pricing as pricing

# Import style 2
from hardware_shop.stock import reduce_stock, OutOfStockError

# Import style 3
from hardware_shop import new_bill_number


# Three customers
customers = [
    {"name": "Rahul", "product": "Cement", "boxes": 4},
    {"name": "Priya", "product": "Paint", "boxes": 25},
    {"name": "Amit", "product": "Hammer", "boxes": 3}
]


# Generate bills
for customer in customers:

    print("\n================================")
    print("       HARDWARE SHOP BILL")
    print("================================")

    try:
        name = customer["name"]
        product = customer["product"]
        boxes = customer["boxes"]

        # Check and reduce stock
        remaining_stock = reduce_stock(product, boxes)

        # Calculate bill
        subtotal, gst, total = pricing.calculate_bill(
            product, boxes
        )

        # Generate bill number
        bill_no = new_bill_number()

        # Display bill
        print("Bill Number :", bill_no)
        print("Customer   :", name)
        print("Product    :", product)
        print("Boxes      :", boxes)
        print("Price      : Rs.", subtotal)
        print("GST (18%)  : Rs.", round(gst, 2))
        print("Total      : Rs.", total)

        print("--------------------------------")
        print("Remaining Stock:", remaining_stock)
        print("Thank you for shopping!")

    except OutOfStockError as error:

        print("Customer :", customer["name"])
        print("Product  :", customer["product"])
        print("Requested Boxes:", customer["boxes"])
        print("Stock Error:", error)
        print("Bill cannot be generated.")

    print("================================")
