import random
list = []
lucky_number = random.randint(0,100)
so_luot = 3
while so_luot > 0:
    number = int(input("Nhap so trong ve vietlott cua ban: "))
    if 0 > number and number > 99:
        print("Nhap so trong khoang (0-99): ")
    else:
        list.append(number)
        so_luot-=1
        print("So luot thu con",so_luot)
print("So may man:",lucky_number)
print("Danh sach so may man cua ban:",list)
if lucky_number in list:
    print("Chuc mung ban da trung thuong!")
else:
    print("Chuc ban may man lan sau!")