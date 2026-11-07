
# Product prices
PRODUCT_PRICES = {
    "Cement": 400,
    "Paint": 250,
    "Hammer": 150,
    "Drill": 1200
}

GST_RATE = 18


# Calculate bill amount
def calculate_bill(product, boxes):

    price = PRODUCT_PRICES[product]

    subtotal = price * boxes

    gst = subtotal * GST_RATE / 100

    total = subtotal + gst

    # Round down to nearest multiple of 5
    final_total = int(total // 5) * 5

    return subtotal, gst, final_total
