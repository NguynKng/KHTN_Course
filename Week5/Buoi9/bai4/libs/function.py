import csv
import datetime
def read_file(_path):
    f = open(_path,"r",encoding="utf-8")
    content = []
    for row in csv.reader(f):
        content.append(row)
    return content

def print_file(content):
    for row in content:
        print("{:20}{:20}{:15}{:20}{:20}{:20}{:20}".format(row[0],row[1],str(row[2]),row[3],str(row[4]),str(row[5]),row[6]))

def add_account(content):
    lst_ma = []
    for row in content:
        lst_ma.append(row[0])
    lst_ma.remove(lst_ma[0])
    ma_hang = input("Nhap ma hang: ")
    if ma_hang not in lst_ma:
        name = input("Nhap ten mat hang: ").title()
        so_luong = int(input("Nhap so luong: "))
        don_vi = input("Nhap don vi tinh: ").title()
        gia_tien = int(input("Nhap gia tien: "))
        thanh_tien = gia_tien*so_luong
        ngay_nhap = datetime.date.today()
        content.append([ma_hang,name,so_luong,don_vi,gia_tien,thanh_tien,ngay_nhap])
        print("Them thanh cong.")
    else:
        print("Ma hang da ton tai.") 
    return content

def update_file(_path,content):
    f = open(_path,"w",encoding="utf-8",newline="")
    csv.writer(f).writerows(content)
    f.close()

def update_account(content):
    ma_hang = input("Nhap ma hang: ")
    for row in content:
        if ma_hang == row[0]:
            print("Truy cập thong tin mat hang thanh cong.")
            name = row[1]
            so_luong = row[2]
            don_vi = row[3]
            gia_tien = row[4]
            while True:
                print("------------Chuong trinh cap nhat thong tin don hang.")
                print("1. Cap nhat ten mat hang.")
                print("2. Cap nhat so luong hang.")
                print("3. Cap nhat don vi tinh.")
                print("4. Cap nhat gia tien.")
                print("0. Quay lai menu.")
                choice = input("Nhap lua chon: ")
                if choice == "1":
                    name = input("Nhap ten mat hang moi: ").title()
                elif choice == "2":
                    so_luong = int(input("Nhap so luong moi: "))
                elif choice == "3":
                    don_vi = input("Nhap don vi tinh moi: ").title()
                elif choice == "4":
                    gia_tien = int(input("Nhap gia hang: "))
                elif choice == "0":
                    break
            row[0] = ma_hang
            row[1] = name
            row[2] = so_luong
            row[3] = don_vi
            row[4] = gia_tien
            row[5] = so_luong*gia_tien
            row[6] = datetime.date.today()
            print("Cap nhat thanh cong.")
            break
    else:
        print("Ma hang khong ton tai, vui long chon them moi.")
    return content
    
def del_account(content):
    ma_hang = input("Nhap ma hang muon xoa: ")
    for row in content:
        if ma_hang == row[0]:
            content.remove(row)
            print('Xoa thanh cong.')
            break
    else:
        print("Ma hang khong ton tai.")
    return content
def search(content):
    max = 0
    kq = []
    for row in content:
        if int(row[2]) > max:
            max = int(row[2])
            row_max = row
    kq = [row_max]
    return kq