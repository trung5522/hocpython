height=int(input("Your height: "))
bill=0
if height >=120:
    print("you can")
    age=int(input("your age: "))
    if age < 12:
        print("5$")
    elif age < 18:
        print("7$")
    else:
        print("12$")
    want_photo= input("do u want take a photo: ")
    if want_photo == "y":
        print("you pay more 3$.")
    else:
        print("thanks")
else:
    print("Cut")