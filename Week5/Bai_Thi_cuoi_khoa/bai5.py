path = "hoadon.csv"
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
        print("{:20}{:20}{:15}{:25}{:20}{:20}".format(row[0],row[1],row[2],row[3],row[4],row[5]))

def update_file(_path,content):
    f = open(_path,"a",encoding="utf-8",newline="")
    csv.writer(f).writerows(content)
    f.close()
def current_ma(content):
    max = 0
    content.pop(0)
    for row in content:
        if int(row[0]) > max:
            max = int(row[0])
    return max + 1

def add_don(content):
    new_order = []
    while True:
        choice = input("Nhan y de them san pham vao don hang: ")
        if choice == "y":
            ma_hd = current_ma(content)
            ma_hang = input("Nhap ma hang: ")
            so_luong = int(input("Nhap so luong: "))
            don_gia = int(input("Nhap don gia: "))
            thanh_tien = so_luong*don_gia
            ngay_mua = datetime.now()
            order_info = [ma_hd,ma_hang,so_luong,don_gia,thanh_tien,ngay_mua]
            new_order.append(order_info)
        else:
            break
    return new_order
def thong_ke(ma_don,content):
    so_luong = 0
    tong_tien = 0
    for row in content:
        if ma_don == row[0]:
            so_luong += int(row[2])
            tong_tien += int(row[4])
    print("{:20}{:20}{:20}".format(ma_don,str(so_luong),str(tong_tien)))
while True:
    print("------------Chuong trinh quan ly thong tin sinh vien.")
    print("1. Xem tat ca don hang dang luu.")
    print("2. Them don hang moi.")
    print("3. Thong ke don hang theo ma.")
    choice = input("Nhap lua chon: ")
    if choice == "1":
        print_file(read_file(path))
    elif choice == "2":
        noi_dung_file = read_file(path)
        noi_dung_moi = add_don(noi_dung_file)
        update_file(path, noi_dung_moi)
        print("LUU THANH CONG.")
    elif choice == "3":
        lst_ma_don = set()
        noi_dung_file = read_file(path)
        noi_dung_file.pop(0)
        for madon in noi_dung_file:
            lst_ma_don.add(madon[0])
        print("Danh sách đơn hàng")
        print("{:20}{:20}{:20}".format("Mã đơn","Số lượng","Tổng tiền"))
        for don in sorted(lst_ma_don):
            thong_ke(don,noi_dung_file)
    else:
        break