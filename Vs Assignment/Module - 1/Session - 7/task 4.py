messages = ['Hi', 'Spam', 'Hello', 'Spam', 'How are you?']

for message in messages:
    if message == 'Spam':
        continue

    if message == 'How are you?':
        break

    print(message)