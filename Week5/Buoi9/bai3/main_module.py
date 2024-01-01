from libs.function import *
file_path = "files/diem.csv"
while True:
    print("------------Chuong trinh quan ly thong tin sinh vien.")
    print("1. Xem danh sach sinh vien.")
    print("2. Them sinh vien.")
    print("3. Cap nhat thong tin sinh vien.")
    print("4. Xoa sinh vien.")
    print("5. Danh sach sinh vien bi rot mon.")
    print("6. Diem trung binh tung mon hoc.")
    print("0. Thoat.")
    choice = input("Nhap lua chon: ")
    if choice == "1":
        print_file(read_file(file_path))
    elif choice == "2":
        noi_dung_file = read_file(file_path)
        noi_dung_moi = add_account(noi_dung_file)
        tiep_tuc = input("Nhap Y de xac nhan luu thong tin sinh vien: ").upper()
        if tiep_tuc == "Y":
            update_file(file_path,noi_dung_moi)
            print("Luu thong tin thanh cong.")
        else:  
            print("Lưu thông tin thất bại.")
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
        tiep_tuc = input("Nhap Y de xac nhan xoa sinh vien: ").upper()
        if tiep_tuc == "Y":
            update_file(file_path,noi_dung_moi)
            print("Xoa sinh vien thanh cong.")
    elif choice == "5":
        noi_dung_file = read_file(file_path)
        tieu_de = noi_dung_file.pop(0)
        ket_qua = lst_rotmon(noi_dung_file)
        if len(ket_qua) > 0:
            print("Co {} ket qua tim thay".format(len(ket_qua)))
            print("------------Danh sach sinh vien rot mon.")
            ket_qua.insert(0,tieu_de)
            print_file(ket_qua)
        else:
            print("Khong tim thay ket qua.")
    elif choice == "6":
        noi_dung_file = read_file(file_path)
        tieu_de = noi_dung_file.pop(0)
        lst_mon = set()
        for row in noi_dung_file:
            lst_mon.add(row[2])
        print("{:20}{:20}{:20}".format("Mã môn","Số lượng","Điểm trung bình"))
        for ma_mon in sorted(lst_mon):
            lst_dtb(ma_mon,noi_dung_file)
    elif choice == "0":
        exit()