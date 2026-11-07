
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_details(self):
        print("Username:", self.username)
        print("Email:", self.email)


user1 = User("vidhya123", "vidhya@gmail.com")
user1.display_details()
