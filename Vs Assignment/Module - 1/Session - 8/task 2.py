def extract_artist(song_title):
    dash_position = song_title.index("-")
    artist = song_title[dash_position + 1:]
    return artist.strip()


song = "Shape of You - Ed Sheeran"

print("Artist:", extract_artist(song))