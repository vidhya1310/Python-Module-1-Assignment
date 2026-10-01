h=int (input("Enter Hight Range :"))

if h>180:
    print("Hight Is too high !")

elif h <= 180 and h >= 175:
    print("Height Is Less Than High !")

elif h <= 170 and h >= 165:
    print("Height Is Normal !")

elif h <= 160 and h >= 155:
    print("Height Is Short !")

elif h <= 150 and h >= 140:
    print("Height Is Too Less !")

else:
    print("Jump")