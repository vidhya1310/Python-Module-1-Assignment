
class Influencer:
    def __init__(self, username, followers):
        self.username = username
        self.followers = followers


class Brand:
    def __init__(self, brand_name):
        self.brand_name = brand_name


class BrandPartner(Influencer, Brand):
    def __init__(self, username, followers, brand_name):
        Influencer.__init__(self, username, followers)
        Brand.__init__(self, brand_name)

    def display_details(self):
        print("Username:", self.username)
        print("Followers:", self.followers)
        print("Brand Name:", self.brand_name)


partner1 = BrandPartner("vidhya123", 50000, "Nike")
partner1.display_details()