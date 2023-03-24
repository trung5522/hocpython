num_char = len(input("what fuck your name?"))
print(type(num_char))
new_num_char= str(num_char)
print("you have " + new_num_char +" characters.")
print(70 + float(100))
print(70 + float("100.5"))
allcharacters=input("nhap 1 so 2 so: ")
first_char=allcharacters[0]
second_char=allcharacters[1]
print(first_char)
print(second_char)
result= first_char+second_char
print(result)
result2=int(first_char)+int(second_char)
print(result2)
# ** la mủ vd 2**3=2^3
weight=input("enter weight: ")
height=input("enter height: ")
bmi=int(weight)/float(height)**2
print(bmi)
bmi_as_int=int(bmi)
print(bmi_as_int)
print(round(8/3,2))
#vd
cccc=0
height=1.8
kiemtra= True
print(f"your ccc is {cccc}, your height {height}, you are {kiemtra}")
age = input("nhap so tuoi ban hien tai: ")
ageconlai= 90-int(age)
songayconlai=ageconlai*365
sogioconlai=songayconlai*24
print(ageconlai)
print(songayconlai)
print(sogioconlai)
#tinh bill
print("tinh tien de...")
total=int(input("Tong bill la: "))
tip=int(input("Ban bo bao nhieu phan tram: "))
people=int(input("So nguoi tham gia tra: "))
tip_as_persent= tip/100
total_pay= (total + total*tip_as_persent)/people
final_pay= round(total_pay, 2)
final_pay= "{:.2f}".format(final_pay)
print(f"Moi nguoi can tra: ${final_pay}")
