playlists = {
    "user1": {
        "Favourites": ["Song1", "Song2"]
    }
}

playlists.setdefault("user2", {})
playlists["user2"].setdefault("Chill", [])

playlists["user2"]["Chill"].append("Song3")

print(playlists)