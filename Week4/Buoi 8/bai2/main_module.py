from libs.function import *
file_path = "files/madinhdanh.csv"
while True:
    print("------------Chuong trinh quan ly thong tin nhan vien.")
    print("1. Xem danh sach tai khoan.")
    print("2. Them tai khoan.")
    print("3. Cap nhat tai khoan.")
    print("4. Xoa tai khoan.")
    print("5. Thong ke danh sach.")
    print("0. Thoat.")
    choice = input("Nhap lua chon: ")
    if choice == "1":
        print_file(read_file(file_path))
    elif choice == "2":
        noi_dung_file = read_file(file_path)
        noi_dung_moi = add_account(noi_dung_file)
        tiep_tuc = input("Nhap Y de xac nhan luu tai khoan: ").upper()
        if tiep_tuc == "Y":
            update_file(file_path,noi_dung_moi)
            print("Luu thong tin thanh cong.")
    elif choice == "3":
        noi_dung_file = read_file(file_path)
        noi_dung_moi= update_account(noi_dung_file)
        tiep_tuc = input("Nhap Y de xac nhan luu tai khoan: ").upper()
        if tiep_tuc == "Y":
            update_file(file_path,noi_dung_moi)
            print("Luu thong tin thanh cong.")
    elif choice == "4":
        noi_dung_file = read_file(file_path)
        noi_dung_moi = del_account(noi_dung_file)
        tiep_tuc = input("Nhap Y de xac nhan xoa tai khoan: ").upper()
        if tiep_tuc == "Y":
            update_file(file_path,noi_dung_moi)
            print("Xoa tai khoan thanh cong.")
    elif choice == "5":
        noi_dung_file = read_file(file_path)
        tieu_de = noi_dung_file.pop(0)
        ket_qua = search_account(noi_dung_file)
        print("Co",len(ket_qua),"ket qua duoc tim thay.")
        if len(ket_qua) > 0:
            ket_qua.insert(0,tieu_de)
            print_file(ket_qua)
    elif choice == "0":
        exit()