
import re

# Function to validate Indian PIN code
def is_valid_pin(text):

    pattern = r"^[1-9][0-9]{5}$"

    if re.match(pattern, text):
        return True
    else:
        return False


# Test PIN codes
print("PIN Code Validation")

print("380015:", is_valid_pin("380015"))
print("110001:", is_valid_pin("110001"))
print("056001:", is_valid_pin("056001"))
print("38001:", is_valid_pin("38001"))
print("3800155:", is_valid_pin("3800155"))
print("38O015:", is_valid_pin("38O015"))
