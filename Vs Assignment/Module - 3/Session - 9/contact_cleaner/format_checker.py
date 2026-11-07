import re
import os

# 1. Validate PIN Code
def is_valid_pin(text):
    pattern = r"^[1-9][0-9]{5}$"
    return re.match(pattern, text) is not None


# 2. Find Mobile Number
def find_mobile(text):
    pattern = r"(?<![0-9])(?:\+91)?[6-9][0-9]{9}(?![0-9])"

    match = re.search(pattern, text)

    if match:
        return match.group()
    else:
        return None


# 3. Count PIN Codes
def count_pins():
    pin_count = {}
    pattern = r"\b[1-9][0-9]{5}\b"

    file_path = os.path.join(os.path.dirname(__file__), "addresses.txt")

    with open(file_path, "r") as file:
        for line in file:
            pins = re.findall(pattern, line)

            for pin in pins:
                if pin in pin_count:
                    pin_count[pin] += 1
                else:
                    pin_count[pin] = 1

    print("\nPIN Code Count:")
    for pin, count in pin_count.items():
        print(pin, ":", count)


# Run tests only when this file is executed directly
if __name__ == "__main__":
    print(is_valid_pin("380015"))
    print(find_mobile("Call 9000012345"))

    count_pins()