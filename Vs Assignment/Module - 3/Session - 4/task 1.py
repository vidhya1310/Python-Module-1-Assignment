class InvalidCouponCodeError(Exception):
    pass


def apply_coupon(coupon_code):
    valid_codes = ["ZOMATO50", "SAVE100", "FOOD20"]

    if coupon_code not in valid_codes:
        raise InvalidCouponCodeError("Invalid coupon code!")

    print("Coupon applied successfully!")


try:
    apply_coupon("ZOMATO50")
    apply_coupon("HELLO10")

except InvalidCouponCodeError as e:
    print(e)