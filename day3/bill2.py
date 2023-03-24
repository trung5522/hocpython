size=input("Do u want how size pizza: S,M,L: ")
bill=0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill +=25
opption=input("do you wanna drink? : ")
if opption == "Y":
    bill +=3
else:
    bill +=1
print(f"You pay for me is $ {bill}")
