
# Available stock
STOCK = {
    "Cement": 10,
    "Paint": 20,
    "Hammer": 15,
    "Drill": 5
}


# Custom exception
class OutOfStockError(Exception):
    pass


# Reduce product stock
def reduce_stock(product, boxes):

    if product not in STOCK:
        raise OutOfStockError("Product not found!")

    if boxes > STOCK[product]:
        raise OutOfStockError(
            f"Only {STOCK[product]} boxes of {product} are available!"
        )

    if boxes <= 0:
        raise OutOfStockError("Boxes must be greater than zero!")

    STOCK[product] -= boxes

    return STOCK[product]
