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
        print("{:20}{:20}{:25}{:20}{:20}{:20}{:20}".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))

def add_account(content):
    lst_ma = []
    for row in content:
        lst_ma.append(row[0])
    lst_ma.remove(lst_ma[0])
    ma_dinh_danh = input("Nhap ma dinh danh: ")
    if ma_dinh_danh not in lst_ma:
        name = input("Nhap ho va ten: ")
        username = input("Nhap username: ")
        pw = input("Nhap password: ")
        sex = input("Nhap gioi tinh: ").title()
        classes = input("Nhap bo phan lam viec: ").title()
        ngay_tao = datetime.now()
        content.append([ma_dinh_danh,name,username,pw,sex,classes,ngay_tao])
        print("Them thanh cong.")
    else:
        print("Ma dinh danh da ton tai.") 
    return content

def update_file(_path,content):
    f = open(_path,"w",encoding="utf-8",newline="")
    csv.writer(f).writerows(content)
    f.close()

def update_account(content):
    ma_dinh_danh = input("Nhap ma dinh danh: ")
    for row in content:
        if ma_dinh_danh == row[0]:
            print("Truy cập tài khoản thành công.")
            name = row[1]
            username = row[2]
            pw = row[3]
            sex = row[4]
            bo_phan = row[5]
            while True:
                print("------------Chuong trinh cap nhat thong tin tai khoan.")
                print("1. Cap nhat ten.")
                print("2. Cap nhat username.")
                print("3. Cap nhat password.")
                print("4. Cap nhat gioi tinh.")
                print("5. Cap nhat bo phan lam viec.")
                print("0. Thoat.")
                choice = input("Nhap lua chon: ")
                if choice == "1":
                    name = input("Nhap ten moi: ").title()
                elif choice == "2":
                    username = input("Nhap username moi: ")
                elif choice == "3":
                    pw = input("Nhap password moi: ")
                elif choice == "4":
                    sex = input("Nhap gioi tinh moi: ").title()
                elif choice == "5":
                    bo_phan = input("Nhap bo phan lam viec moi: ").title()
                elif choice == "0":
                    break
            row[0] = ma_dinh_danh
            row[1] = name
            row[2] = username
            row[3] = pw
            row[4] = sex
            row[5] = bo_phan
            row[6] = datetime.now()
            print("Cap nhat thanh cong.")
            break
    else:
        print("Ma dinh danh khong ton tai, vui long chon them moi.")
    return content
    
def del_account(content):
    ma_dinh_danh = input("Nhap ma dinh danh: ")
    for row in content:
        if ma_dinh_danh == row[0]:
            username = input("Nhap username: " )
            if username == row[2]:
                pw = input("Nhap password: ")
                if pw == row[3]:
                    content.remove(row)
                    print('Xoa thanh cong.')
                    break
                else:
                    print("Password sai.")
                    break
            else:
                print("Username khong ton tai.")
                break
    else:
        print("Ma dinh danh khong ton tai.")
    return content
def search_account(content):
    bo_phan = input("Nhap bo phan lam viec: ")
    kq = []
    for row in content:
        if bo_phan == row[5]:
               kq.append(row)
    return kq