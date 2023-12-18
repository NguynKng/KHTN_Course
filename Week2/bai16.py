danh_ba = {
    '0989741258':'Johnny',
    '0903852147':'Katherine',
    '0903712712':'Johnny'
}
while True:
    print("Chương trình quản lý điện thoại")
    print("1: Xem danh bạ")
    print("2: Cập nhật danh bạ")
    print("3: Thêm liên hệ")
    print("4: Xóa liên hệ")
    print("5: Tìm liên hệ")
    choice = input("Nhập lựa chọn: ")
    if choice == "1":
        print("{:15}{:15}".format("SĐT\n","Tên\n"))
        for k, v in danh_ba.items():
            print("{:15}{:15}".format(k,v))
    elif choice == "2":
        sdt = input("Nhập sđt cần cập nhật: ")
        if sdt in danh_ba:
            ten = input("Nhập tên cần cập nhật: ")
            danh_ba[sdt] = ten
            print("Cập nhật thành công!")
        else:
            print("SĐT không tồn tại, vui lòng chọn chức năng thêm liên hệ")
    elif choice == "3":
        while True:
            new_phone = input("Nhập sđt muốn thêm: ")
            if new_phone in danh_ba:
                new_name = input("Nhập tên muốn thêm: ")
                danh_ba[new_phone] = new_name
                print("Thêm liên hệ thành công!")
                break
            else:
                print("SĐT không tồn tại, vui lòng nhập lại!")
    elif choice == "4":
       while True:
            sdt = input("Nhập sđt muốn xóa: ")
            if sdt in danh_ba:
                del(danh_ba[sdt])
                break
            else:
                print("SĐT không tồn tại.")
    elif choice == "5":
        ten = input("Nhập tên liên hệ muốn tìm: ")
        ket_qua = {}
        for k,v in danh_ba.items():
            if ten == v:
                ket_qua[k] = v
        if len(ket_qua) > 0:
            print("Có",len(ket_qua),"kết quả.")
            print("{:15}{:15}".format("SĐT","Tên"))
            for k, v in ket_qua.items():
                print("{:15}{:15}".format(k,v))
        else:
            print(f"{ten} không tìm thấy kết quả.")
    else:
        break