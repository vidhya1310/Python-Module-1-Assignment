from playlist import add_song, remove_song, display_playlist

playlist = []

playlist = add_song("Kesariya", playlist)
playlist = add_song("Rabata", playlist)
playlist = add_song("Berian", playlist)

print("My Playlist:")
display_playlist(playlist)

playlist = remove_song("Berian", playlist)

print("\nUpdated Playlist:")
display_playlist(playlist)