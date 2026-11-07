import random

songs = [
    "Kesariya",
    "Tum Hi Ho",
    "Apna Bana Le",
    "Channa Mereya",
    "Raataan Lambiyan"
]

random.shuffle(songs)

print("My Shuffled Playlist:")

for song in songs:
    print(song)