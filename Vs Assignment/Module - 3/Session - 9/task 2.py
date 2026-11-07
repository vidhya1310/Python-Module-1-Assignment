
import re

# Function to validate PIN code
def is_valid_pin(text):
    pattern = r"^[1-9][0-9]{5}$"

    if re.match(pattern, text):
        return True
    else:
        return False


# Function to find Indian mobile number
def find_mobile(text):

    pattern = r"(?<![0-9])(?:\+91)?[6-9][0-9]{9}(?![0-9])"

    match = re.search(pattern, text)

    if match:
        return match.group()
    else:
        return None


# Test mobile numbers
print("Mobile Number Testing")

print(find_mobile("Call 9000012345 after 6 pm"))
print(find_mobile("Reach me on +919000012345"))
print(find_mobile("Flat 5000012345"))
print(find_mobile("Ring 900001234"))
