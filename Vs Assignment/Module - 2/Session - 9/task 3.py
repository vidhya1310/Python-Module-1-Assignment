users = [('vidhya', 200), ('aksha', 50), ('yushra', 120)]

result = list(filter(lambda x: x[1] > 100, users))

for user in result:
    print(user[0])