
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

    def display_details(self):
        print("Username:", self.username)
        print("Email:", self.email)
        print("Followers:", self.followers)
        print("Badge:", self.badge)


verified1 = VerifiedInfluencer(
    "vidhya123", "vidhya@gmail.com", 150000, "Blue Tick"
)

verified1.display_details()