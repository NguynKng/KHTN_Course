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
        print("{:20}{:30}{:15}{:30}{:20}{:20}".format(row[0],row[1],row[2],row[3],str(row[4]),row[5]))

def add_account(content):
    lst_ma = []
    for row in content:
        lst_ma.append(row[0])
    lst_ma.remove(lst_ma[0])
    mssv = input("Nhap MSSV: ")
    if mssv not in lst_ma:
        name = input("Nhap ho va ten: ").upper()
        ma_mh = input("Nhap ma mon hoc: ")
        ten_mh = input("Nhap ten mon hoc: ").upper()
        diem = float(input("Nhap diem mon hoc: "))
        ngay_tao = datetime.now()
        content.append([mssv,name,ma_mh,ten_mh,diem,ngay_tao])
        print("Them thanh cong.")
    else:
        print("Ma so sinh vien da ton tai.") 
    return content

def update_file(_path,content):
    f = open(_path,"w",encoding="utf-8",newline="")
    csv.writer(f).writerows(content)
    f.close()

def update_account(content):
    mssv = input("Nhap MSSV: ")
    for row in content:
        if mssv == row[0]:
            print("Truy cập thong tin sinh vien thanh cong.")
            name = row[1]
            ma_mh = row[2]
            ten_mh = row[3]
            diem = row[4]
            ngay_tao = datetime.now()
            while True:
                print("------------Chuong trinh cap nhat thong tin sinh vien.")
                print("1. Cap nhat ten.")
                print("2. Cap nhat ma mon hoc.")
                print("3. Cap nhat ten mon hoc.")
                print("4. Cap nhat diem.")
                print("0. Thoat.")
                choice = input("Nhap lua chon: ")
                if choice == "1":
                    name = input("Nhap ten moi: ").upper()
                elif choice == "2":
                    ma_mh = input("Nhap ma mon hoc moi: ")
                elif choice == "3":
                    ten_mh = input("Nhap ten mon hoc moi: ").upper()
                elif choice == "4":
                    diem = float(input("Nhap diem mon hoc moi: "))
                elif choice == "0":
                    break
            row[0] = mssv
            row[1] = name
            row[2] = ma_mh
            row[3] = ten_mh
            row[4] = diem
            row[5] = ngay_tao
            print("Cap nhat thanh cong.")
            break
    else:
        print("Ma so sinh vien khong ton tai, vui long chon them moi.")
    return content
    
def del_account(content):
    mssv = input("Nhap ma sinh vien: ")
    for row in content:
        if mssv == row[0]:
            content.remove(row)
            print('Xoa thanh cong.')
            break
    else:
        print("Ma sinh vien khong ton tai.")
    return content
def lst_rotmon(content):
    ten_mh = input("Nhap ten mon hoc: ").upper()
    kq = []
    for row in content:
        if ten_mh == row[3] and float(row[4]) < 5:
            kq.append(row)
    return kq
def lst_dtb(ma_mon,content):
    so_luong = 0
    diem = 0
    for row in content:
        if ma_mon == row[2]:
            so_luong += 1
            diem += float(row[4])
    dtb = round(diem / so_luong,2)
    print("{:20}{:20}{:20}".format(ma_mon,str(so_luong),str(dtb)))