user_bio = "Music lover | Foodie | Traveller"

count = 0

for character in user_bio:
    if character != " ":
        count = count + 1

print("Number of characters excluding spaces:", count)