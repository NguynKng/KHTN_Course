hoa_don={
    'SP001':['Bút bi Thiên Long',30,12000],
    'SP002':['Vở kẻ ngang Vĩnh Tiến',10,32000]
}
def print_board(hoa_don):
    sum = 0
    print("CHI TIET HOA DON")
    print("{:15}{:30}{:20}{:20}{:20}".format("Mã hàng","Tên hàng","Số lượng","Đơn giá",'Thành tiền'))
    for item in hoa_don:
        thong_tin = hoa_don[item]
        ten_hang = thong_tin[0]
        so_luong = thong_tin[1]
        don_gia = thong_tin[2]
        thanh_tien = so_luong*don_gia
        sum += thanh_tien
        print("{:15}{:30}{:20}{:20}{:20}".format(item,ten_hang,str(so_luong),str(don_gia),str(thanh_tien)))
    print("-----------")
    print("Tổng: ",sum)

def add_hoa_don(hoa_don):
    ma_don = input("Nhap ma hang: ")
    if ma_don in hoa_don:
        print("Ma hang da ton tai.")
    else:
        ten_hang = input("Nhap ten mat hang: ")
        so_luong = int(input("Nhap so luong: "))
        don_gia = int(input("Nhap don gia: "))
        hoa_don[ma_don] = [ten_hang,so_luong,don_gia]
        print("Them thanh cong.")
    return hoa_don
def xoa_don(hoa_don):
    ma_hang = print("Nhap ma hang can xoa: ")
    for item in hoa_don:
        if ma_hang == item:
            del hoa_don[item]
    else:
        print("Khong tim thay ma hang.")
    return hoa_don
while True:
    print("--------Chương trình quản lí kết quả học tập sinh viên.")
    print("1. Xem chi tiết hóa đơn.")
    print("2. Thêm sản phẩm mới.")
    print("3. Xóa sản phẩm.")
    print("0. Thoát")
    choice = input("Nhap lua chon: ")
    if choice == "1":
        print_board(hoa_don)
    elif choice == "2":
        add_hoa_don(hoa_don)
    elif choice == "3":
        xoa_don(hoa_don)
    elif choice == "0":
        exit()