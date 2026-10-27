import math

bill = 850
discount = bill * 10 / 100
final_bill = bill - discount

print("Original Bill:", bill)
print("Discount:", discount)
print("Final Bill:", math.floor(final_bill))