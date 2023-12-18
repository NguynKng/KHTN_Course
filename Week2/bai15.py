tup_can = "Canh","Tan","Nham","Quy","Giap","At","Binh","Dinh",
tup_chi = "Than","Dau","Tuat","Hoi","Ti","Suu","Dan","Mao","Thin","Ty","Ngo","Mui"
while True:
    input = int(input("Nhap nam duong lich: "))
    if input > 0:
        break
can = input % 10
chi = input % 12
can_chi = str(tup_can[can]) + " " + str(tup_chi[chi])
print(input,"là năm",can_chi)