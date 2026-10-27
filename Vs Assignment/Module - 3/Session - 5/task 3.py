class InstagramPost:
    def __init__(self, caption, likes, comments):
        self.caption = caption
        self.likes = likes
        self.comments = comments

    def add_comment(self, comment_text):
        self.comments.append(comment_text)
        self.likes += 1

    def show_post(self):
        print("Caption:", self.caption)
        print("Likes:", self.likes)
        print("Comments:", self.comments)


post1 = InstagramPost(
    "Enjoying my day!",
    10,
    ["Beautiful photo!", "Amazing!"]
)

post1.add_comment("Lovely picture!")

post1.show_post()