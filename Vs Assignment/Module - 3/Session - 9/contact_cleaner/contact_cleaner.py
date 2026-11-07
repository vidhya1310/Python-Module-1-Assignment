import os
from format_checker import is_valid_pin, find_mobile

# Get current folder path
folder_path = os.path.dirname(__file__)

# Read contacts.txt
input_file = os.path.join(folder_path, "contacts.txt")

with open(input_file, "r") as file:
    contacts = file.readlines()


# Create empty lists
valid_contacts = []
rejected_contacts = []


# Check every contact
for contact in contacts:
    contact = contact.strip()

    # Skip blank lines
    if not contact:
        continue

    # Split contact details
    parts = contact.split(",")

    # Check exactly 3 values
    if len(parts) != 3:
        rejected_contacts.append(contact + " - Invalid Format")
        continue

    name, mobile, pin = parts

    reasons = []

    if find_mobile(mobile) != mobile:
        reasons.append("Invalid Mobile Number")

    if not is_valid_pin(pin):
        reasons.append("Invalid PIN Code")

    if len(reasons) == 0:
        valid_contacts.append(contact)
    else:
        rejected_contacts.append(
            contact + " - " + ", ".join(reasons)
        )


# Create valid_contacts.txt
valid_file = os.path.join(
    folder_path, "valid_contacts.txt"
)

with open(valid_file, "w") as file:

    for contact in valid_contacts:
        file.write(contact + "\n")


# Create rejected_contacts.txt
rejected_file = os.path.join(
    folder_path, "rejected_contacts.txt"
)

with open(rejected_file, "w") as file:

    for contact in rejected_contacts:
        file.write(contact + "\n")


# Display final result
print("\nCONTACT CLEANING COMPLETED")

print("Total Contacts:", len(contacts))
print("Valid Contacts:", len(valid_contacts))
print("Rejected Contacts:", len(rejected_contacts))

print("\nValid contacts saved successfully!")
print("Rejected contacts saved successfully!")
