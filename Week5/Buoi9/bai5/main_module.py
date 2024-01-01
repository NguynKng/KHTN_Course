from libs.function import *
file_path = "files/donhang.csv"
while True:
    print("------------Chuong trinh quan ly thong tin don hang.")
    print("1. Xem danh sach don hang.")
    print("2. Them moi don hang.")
    print("3. Thong ke don hang.")
    print("0. Thoat.")
    choice = input("Nhap lua chon: ")
    if choice == "1":
        print_file(read_file(file_path))
    elif choice == "2":
        noi_dung_file = read_file(file_path)
        noi_dung_moi = add_account(noi_dung_file)
        tiep_tuc = input("Nhap Y de xac nhan luu thong tin don hang: ").upper()
        if tiep_tuc == "Y":
            update_file(file_path,noi_dung_moi)
            print("Luu thong tin don hang thanh cong.")
        else:  
            print("Lưu thông tin don hang thất bại.")
    elif choice == "3":
        lst_ma_don = set()
        noi_dung_file = read_file(file_path)
        noi_dung_file.pop(0)
        for madon in noi_dung_file:
            lst_ma_don.add(madon[0])
        print("Danh sách đơn hàng")
        print("{:20}{:20}{:20}".format("Mã đơn","Số lượng","Tổng tiền"))
        for don in sorted(lst_ma_don):
            thong_ke(don,noi_dung_file)
    elif choice == "0":
        exit()