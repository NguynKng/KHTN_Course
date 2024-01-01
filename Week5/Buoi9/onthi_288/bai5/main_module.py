from libs.function import *
file_path = "files/account.csv"
while True:
    print("------------Chuong trinh quan ly thong tin sinh vien.")
    print("1. Xem danh sach tai khoan.")
    print("2. Doi mat khau cho tai khoan.")
    print("0. Thoat.")
    choice = input("Nhap lua chon: ")
    if choice == "1":
        print_file(read_file(file_path))
    elif choice == "2":
        noi_dung_file = read_file(file_path)
        noi_dung_moi = change_pw(noi_dung_file)
        tiep_tuc = input("Nhap Y de xac nhan luu thong tin tai khoan: ").upper()
        if tiep_tuc == "Y":
            update_file(file_path,noi_dung_moi)
            print("Luu thong tin thanh cong.")
        else:  
            print("Lưu thông tin thất bại.")
    elif choice == "0":
        exit()