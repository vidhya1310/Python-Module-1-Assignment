def book_movie_ticket(movie_name, seat_type="Regular", snacks=None):
    print("Movie:", movie_name)
    print("Seat:", seat_type)
    print("Snacks:", snacks)

# Positional arguments
book_movie_ticket("Jawan", "VIP", "Popcorn")

# Keyword arguments
book_movie_ticket(movie_name="Pathaan", seat_type="Regular", snacks="Pizza")

# Mix of positional and keyword arguments
book_movie_ticket("Jawan", snacks="Burger", seat_type="VIP")