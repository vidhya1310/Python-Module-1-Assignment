
team = {"CSK": {"captain": "Dhoni","players": 18 },
    "MI": {"captain": "Rohit","players": 17}}

team["GT"] = {"captain": "Gil","players": 16}

for team_name, details in team.items():
    print(team_name, "-", details["captain"])
