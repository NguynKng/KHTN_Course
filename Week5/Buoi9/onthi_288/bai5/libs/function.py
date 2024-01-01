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
        print("{:20}{:20}{:15}{:25}{:20}{:20}".format(row[0],row[1],row[2],row[3],str(row[4]),row[5]))

def update_file(_path,content):
    f = open(_path,"w",encoding="utf-8",newline="")
    csv.writer(f).writerows(content)
    f.close()

def change_pw(content):
    username = input("Nhap username: ")
    for row in content:
        if username == row[1]:
            old_pw = input("Nhap password: ")
            if old_pw == row[2]:
                new_pw = input("Nhap password mới: ")
                if new_pw == old_pw:
                    print("Mat khau moi trung voi mat khau cu.")
                else:
                    row[2] = new_pw
                    print("Doi mat khau thanh cong.")
                    break
            else:
                print("Mật khẩu cũ không đúng.")
                break
    else:
        print("Username khong ton tai.")
    return content