teams = ["CSK", "MI", "RCB", "GT", "KKR"]
points = [12, 8, 15, 10, 14]

ipl = dict(zip(teams, points))

for team, point in ipl.items():
    if point > 10:
        print(team, ":", point)