
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers

    def display_details(self):
        print("Username:", self.username)
        print("Email:", self.email)
        print("Followers:", self.followers)


influencer1 = Influencer("vidhya123", "vidhya@gmail.com", 15000)
influencer1.display_details()