def apply_coupon(amount, coupon_code=None):
    if coupon_code == "SAVE10":
        amount = amount * 0.90

    return amount

print(apply_coupon(1000, "SAVE10"))
print(apply_coupon(1000))