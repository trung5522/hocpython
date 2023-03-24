weight=float(input("Your weight in kg: "))
height=float(input("Your height in m: "))
bmi=round(weight/height**2, 2)
#bmi="{:.2f}".format(bmi)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, nomalweight")
elif bmi < 30:
    print(f"Your bmi is {bmi}, overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, obese")
else:
    print(f"Your bmi is {bmi}, clinically obese")