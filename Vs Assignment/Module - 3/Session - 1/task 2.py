# Read songs with line numbers

file = open("my_fav_songs.txt", "r")

for line_number, song in enumerate(file, start=1):
    print(line_number, song.strip())

file.close()