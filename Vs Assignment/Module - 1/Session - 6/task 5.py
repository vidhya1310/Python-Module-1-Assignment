row = 1

while row <= 7:
    spaces = 7 - row

    while spaces > 0:
        print(" ", end="")
        spaces = spaces - 1

    stars = 1

    while stars <= (2 * row - 1):
        print("*", end="")
        stars = stars + 1

    print()
    row = row + 1