w= int (input("Enter weather temparature :"))

if w>100:
    print("Weather is too Hot !")

elif w <= 100 and w >= 80:
    print("Weather Is Less Than High !")

elif w <= 70 and w >= 65:
    print("Weather Is Normal !")

elif w <= 50 and w >= 30:
    print("Weather Is cold !")

elif w <= 30 and w >= 10:
    print("Weather Is Too Less !")

else:
    print("Freeze")