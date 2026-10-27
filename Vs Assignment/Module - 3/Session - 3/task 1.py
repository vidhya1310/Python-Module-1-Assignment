def get_song_duration(song_name):
    songs = {
        "Kesariya": "4:28",
        "Apna Bana Le": "4:21",
        "Tum Hi Ho": "4:22",
        "Heeriye": "3:15"
    }

    try:
        return songs[song_name]
    except KeyError:
        print("Song not found on Spotify!")


print(get_song_duration("Kesariya"))
get_song_duration("Believer")