class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration


song1 = Song("Kesariya", "Arijit Singh", 268)
song2 = Song("Heeriye", "Arijit Singh", 195)

print(song1.title, song1.artist, song1.duration)
print(song2.title, song2.artist, song2.duration)