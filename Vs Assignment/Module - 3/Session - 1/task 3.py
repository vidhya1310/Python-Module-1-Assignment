# Add 2 songs without deleting existing songs

file = open("my_fav_songs.txt", "a")

file.write("Tera Ban Jaunga\n")
file.write("Raataan Lambiyan\n")

file.close()

print("Two songs added successfully!")