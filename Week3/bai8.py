def xem_goi_cuoc(du_lieu):
    print("{:15}{:15}{:15}{:15}".format("Ma goi","Gia tien","Dung luong","Thoi han"))
    for k,v in du_lieu.items():
        print("{:15}{:15}{:15}{:15}{:15}".format(k,str(v[0]),str(v[1]),str(v[2]),"VND/GB/ngay"))

def them_goi(du_lieu):
    ten_goi = input("Nhap ten goi muon them: ")
    if ten_goi in du_lieu:
        print("Ten goi da ton tai.")
    else:
        gia_tien = int(input("Gia goi: "))
        dung_luong = float(input("Dung luong: "))
        thoi_han = int(input("Thoi han:"))
        du_lieu[ten_goi] = [gia_tien,dung_luong,thoi_han]
        print("Them goi thanh cong.")
def cap_nhat(du_lieu):
    ten_goi = input("Nhap ten goi cuoc can cap nhat: ")
    if ten_goi in du_lieu:
        while True:
            print("1. Cap nhat gia goi cuoc.")
            print("2. Cap nhat dung luong.")
            print("3. Cap nhat thoi han goi cuoc.")
            print("0. Thoat")
            choice = input("Nhap chuc nang so can cap nhat: ")
            du_lieu1 = du_lieu[ten_goi]
            gia_tien = du_lieu1[0]
            dung_luong = du_lieu1[1]
            thoi_han = du_lieu1[2]
            if choice == "1":
                gia_tien = int(input("Gia goi: "))
                du_lieu[ten_goi] = [gia_tien,dung_luong,thoi_han]
            elif choice == "2":
                dung_luong = float(input("Dung luong: "))
                du_lieu[ten_goi] = [gia_tien,dung_luong,thoi_han]
            elif choice == "3":
                thoi_han = int(input("Thoi han"))
                du_lieu[ten_goi] = [gia_tien,dung_luong,thoi_han]
            elif choice == "0":
                break
            else:
                print("Lua chon khong hop le, nhap lai.")
    else:
        print("Ten goi khong ton tai hoac khong hop le.")
def tinh_dl(du_lieu,ten_goi):
    du_lieu1 = du_lieu[ten_goi]
    return du_lieu1[1]/du_lieu1[2]

goi_cuoc = {
    'D3': [15000,3,3],
    'DT30': [30000,7,7],
    'M50': [50000,1.2,30]
}
while True:
    print("Chuong trinh quan li goi cuoc di dong.")
    print("1. Xem goi cuoc.")
    print("2. Them goi cuoc moi vao he thong.")
    print("3. Cap nhat thong tin goi cuoc.")
    print("4. Tinh dung luong trung binh goi cuoc.")
    choice = input("Nhap lua chon: ")
    if choice == "1":
        xem_goi_cuoc(goi_cuoc)
    elif choice == "2":
        them_goi(goi_cuoc)
    elif choice == "3":
        cap_nhat(goi_cuoc)
    elif choice == "4":
        ten_goi = input("Nhap ten goi muon xem dung luong/ngay: ")
        if ten_goi in goi_cuoc:
            print("Dung luong goi cuoc {} la {}GB/ngay".format(ten_goi,tinh_dl(goi_cuoc,ten_goi)))
        else:
            print("Goi cuoc khong ton tai hoac khong hop le.")