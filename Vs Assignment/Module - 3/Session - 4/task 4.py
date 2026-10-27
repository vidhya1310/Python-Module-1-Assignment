class InvalidSeatNumberError(Exception):
    pass


def book_ticket(movie_name, seat_number):
    if seat_number <= 0:
        raise InvalidSeatNumberError(
            "Seat number must be positive"
        )

    print("Ticket booked successfully for", movie_name)


try:
    book_ticket("Avengers", -2)

except InvalidSeatNumberError as e:
    print("Error:", e)