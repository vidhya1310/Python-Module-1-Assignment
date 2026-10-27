from playlist import add_song, remove_song

playlist = []

playlist = add_song("Kesariya", playlist)
playlist = add_song("Rabata", playlist)
playlist = add_song("Berian", playlist)

print("Original Playlist:", playlist)

playlist = remove_song("Shape of You", playlist)

print("Updated Playlist:", playlist)