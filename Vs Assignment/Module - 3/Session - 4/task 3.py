class PaymentFailedError(Exception):
    pass


def process_payment(amount):
    if amount <= 0:
        raise PaymentFailedError("Payment amount must be greater than zero!")

    print("Payment Successful")


try:
    process_payment(500)
    process_payment(-100)

except PaymentFailedError as e:
    print(e)