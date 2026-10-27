def format_likes(count):
    if count >= 1000000:
        return str(round(count / 1000000, 1)) + "M"

    elif count >= 1000:
        return str(round(count / 1000, 1)) + "K"

    else:
        return count