def reverse_message(message):
    reversed_text = ""

    for character in message:
        reversed_text = character + reversed_text

    return reversed_text


text = input("Enter a message: ")

print("Reversed message:", reverse_message(text))