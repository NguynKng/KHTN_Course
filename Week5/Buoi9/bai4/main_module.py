from libs.function import *
file_path = "files/quanlykho.csv"
while True:
    print("------------Chuong trinh quan ly thong tin don hang.")
    print("1. Xem danh sach mat hang.")
    print("2. Them mat hang.")
    print("3. Cap nhat thong tin mat hang.")
    print("4. Xoa mat hang.")
    print("5. Loc mat hang co so luong nhieu nhat.")
    print("0. Thoat.")
    choice = input("Nhap lua chon: ")
    if choice == "1":
        print_file(read_file(file_path))
    elif choice == "2":
        noi_dung_file = read_file(file_path)
        noi_dung_moi = add_account(noi_dung_file)
        tiep_tuc = input("Nhap Y de xac nhan luu thong tin mat hang: ").upper()
        if tiep_tuc == "Y":
            update_file(file_path,noi_dung_moi)
            print("Luu thong tin thanh cong.")
        else:  
            print("Lưu thông tin thất bại.")
    elif choice == "3":
        noi_dung_file = read_file(file_path)
        noi_dung_moi= update_account(noi_dung_file)
        tiep_tuc = input("Nhap Y de xac nhan luu thong tin: ").upper()
        if tiep_tuc == "Y":
            update_file(file_path,noi_dung_moi)
            print("Luu thong tin thanh cong.")
        else:
            print("Luu thong tin that bai.")
    elif choice == "4":
        noi_dung_file = read_file(file_path)
        noi_dung_moi = del_account(noi_dung_file)
        tiep_tuc = input("Nhap Y de xac nhan xoa mat hang: ").upper()
        if tiep_tuc == "Y":
            update_file(file_path,noi_dung_moi)
            print("Xoa mat hang thanh cong.")
        else:
            print("Xoa mat hang that bai.")
    elif choice == "5":
        noi_dung_file = read_file(file_path)
        tieu_de = noi_dung_file.pop(0)
        ket_qua = search(noi_dung_file)
        ket_qua.insert(0,tieu_de)
        print_file(ket_qua)
    elif choice == "0":
        exit()