def video_views(titles, views):
    result = [
        (title, round(count, -3))
        for title, count in zip(titles, views)
    ]
    return result

titles = ["Python Tutorial", "Django Tutorial", "SQL Tutorial"]
views = [125600, 98750, 234400]
result = video_views(titles, views)
print(result)
