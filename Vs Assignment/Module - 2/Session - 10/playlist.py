def add_song(song_name, playlist):
    playlist.append(song_name)
    return playlist


def remove_song(song_name, playlist):
    if song_name in playlist:
        playlist.remove(song_name)
    return playlist


def display_playlist(playlist):
    for i, song in enumerate(playlist, start=1):
        print(i, song)

def display_playlist(playlist):
    i = 1

    for song in playlist:
        print(i, song)
        i = i + 1