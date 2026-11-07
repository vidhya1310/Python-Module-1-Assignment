
def format_followers(count):
    if count >= 1000000:
        return f"{count / 1000000:.1f}M"
    elif count >= 1000:
        return f"{count / 1000:.1f}K"
    else:
        return str(count)


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers


class VerifiedInfluencer(Influencer):
    def __init__(self, username, email, followers, badge):
        super().__init__(username, email, followers)
        self.badge = badge

    def display_profile(self):
        print("Instagram Profile")
        print("-----------------")
        print("Username:", self.username)
        print("Followers:", format_followers(self.followers))
        print("Verified Badge:", self.badge)


verified1 = VerifiedInfluencer(
    "vidhya123", "vidhya@gmail.com", 1500000, "Blue Tick"
)

verified1.display_profile()