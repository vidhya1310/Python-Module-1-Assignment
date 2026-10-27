# Count total songs in the file

file = open("my_fav_songs.txt", "r")

songs = file.readlines()

total = len(songs)

file.close()

print("Total songs:", total)