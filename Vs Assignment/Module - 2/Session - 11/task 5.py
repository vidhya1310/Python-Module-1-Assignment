import random

songs = [
    "Kesariya",
    "Rabata",
    "Berian",
    "Tum Prem Ho",
    "Tum Tak",
    "Chand Ne Kaho",
    "Apna Bana Le",
    "Tum Hi Ho"
]

playlist = random.sample(songs, 3)

print("Today's Playlist:")

for song in playlist:
    print(song)