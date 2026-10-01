def display_friends(friends): 

    for username, followers in friends.items(): 

        print(username, ":", followers, "followers") 

friends = { "Vidhya": "5.5K", "Aksha": "5.3K", "Yushra": "4.7K", "Kashish" :"4.5" ,"Maitri" :"3.0" } 

display_friends(friends)