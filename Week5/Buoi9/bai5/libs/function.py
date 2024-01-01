import csv
from datetime import datetime
def read_file(_path):
    f = open(_path,"r",encoding="utf-8")
    content = []
    for row in csv.reader(f):
        content.append(row)
    return content

def print_file(content):
    for row in content:
        print("{:20}{:20}{:15}{:20}{:20}{:20}{:20}".format(row[0],row[1],str(row[2]),row[3],str(row[4]),str(row[5]),row[6]))

def current_ma(content):
    max = 0
    content.pop(0)
    for row in content:
        if int(row[0]) > max:
            max = int(row[0])
    return max + 1

def add_account(content):
    new_order = []
    ma_don = current_ma(content)
    menu = {
        "1": ["Gà rán",45000,"miếng"],
        "2": ["Coca Cola",14000,"chai"],
        "3": ["Khoai tây chíp",45000,"gram"],
        "4": ["Xiên que đồng giá",15000,"que"]
    }
    while True:
        print("--------Chọn thực đơn.")
        print("1. Gà rán.")
        print("2. Coca Cola.")
        print("3. Khoai tây chíp.")
        print("4. Xiên que đồng giá.")
        print("0. Ket thuc.")
        choice = input("Nhap lua chon: ")
        if choice == "1":
            thong_tin = menu[choice]
        elif choice == "2":
            thong_tin = menu[choice]
        elif choice == "3":
            thong_tin = menu[choice]
        elif choice == "4":
            thong_tin = menu[choice]
        elif choice == "0":
            break
        ten_tp = thong_tin[0]
        gia = thong_tin[1]
        dvt = thong_tin[2]
        so_luong = int(input("Nhap so luong: "))
        thanh_tien = gia*so_luong
        ngay_order = datetime.now()
        order_info = [ma_don,ten_tp,so_luong,dvt,gia,thanh_tien,ngay_order]
        new_order.append(order_info)
        print("Luu thong tin mat hang thanh cong.")
    return new_order

def update_file(_path,content):
    f = open(_path,"a",encoding="utf-8",newline="")
    csv.writer(f).writerows(content)
    f.close()

def thong_ke(ma_don,content):
    so_luong = 0
    tong_tien = 0
    for row in content:
        if ma_don == row[0]:
            so_luong += int(row[2])
            tong_tien += int(row[5])
    print("{:20}{:20}{:20}".format(ma_don,str(so_luong),str(tong_tien)+" VNĐ"))