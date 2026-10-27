# Create a file and write 5 songs

file = open("my_fav_songs.txt", "w")

file.write("Kesariya\n")
file.write("Apna Bana Le\n")
file.write("Tum Hi Ho\n")
file.write("Chaleya\n")
file.write("Heeriye\n")

file.close()

print("Songs written successfully!")