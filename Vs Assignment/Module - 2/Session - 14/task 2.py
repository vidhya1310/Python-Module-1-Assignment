def add_song_to_playlist(playlists, user, playlist_name, song_title, artist):
    playlists.setdefault(user, {})
    playlists[user].setdefault(playlist_name, [])

    song = {"title": song_title, "artist": artist}
    playlists[user][playlist_name].append(song)


playlists = {}

add_song_to_playlist(playlists, "vidhya", "Favourites", "Kesariya", "Arijit Singh")
add_song_to_playlist(playlists, "vidhya", "Favourites", "Tum Hi Ho", "Arijit Singh")
add_song_to_playlist(playlists, "rahul", "Chill", "Perfect", "Ed Sheeran")

print(playlists)