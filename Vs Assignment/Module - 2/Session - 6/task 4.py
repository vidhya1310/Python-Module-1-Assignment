titles = ["3 Idiots", "Dangal", "Pathaan"]
genres = ["Comedy", "Sports", "Action"]
ratings = [8.4, 8.3, 7.0]

movies = []

for title, genre, rating in zip(titles, genres, ratings):
    movie = {"title": title,"genre": genre,"rating": rating}
    
    movies.append(movie)

print(movies)