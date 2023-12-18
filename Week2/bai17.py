tu_dien={
    'one':['số 1','con số 1'],
    'father':['cha','bố']
}
while True:
    print("Chương trình quản lý từ điển Anh-Việt.")
    print("1: Xem từ điển.")
    print("2: Cập nhật lại nghĩa Tiếng Việt.")
    print("3: Thêm vào từ điển.")
    print("4: Xóa từ ra khỏi từ điển.")
    print("0: Chọn để thoát")
    choice = input("Nhập lựa chọn: ")
    if choice == "1":
        print("Từ điển Anh-Việt.")
        print("{:25}{:25}".format("English","Vietnamese"))
        for k, v in tu_dien.items():
            print("{:25}{:25}".format(k,", ".join(v)))
    elif choice == "2":
        tu_anh = input("Nhập từ Tiếng Anh muốn cập nhật: ").lower()
        if tu_anh in tu_dien:
            nghia = tu_dien[tu_anh]
            nghia_moi = input("Nhập nghĩa mới muốn cập nhật cách nhau bởi dấu ,: ").lower()
            lst_moi = nghia_moi.split(',')
            nghia.extend(lst_moi)
            tu_dien[tu_anh] = nghia
            print("Cập nhật thành công!.")
        else:
            print("Không tìm thấy kết quả ",f"{tu_anh}.")
    elif choice == "3":
        tu_anh = input("Nhập từ Anh muốn thêm: ").lower()
        if tu_anh in tu_dien:
            tu_viet = input("Nhập nghĩa muốn thêm cách nhau bởi dấu ,: ")
            lst_moi = tu_viet.split(',')
            tu_dien[tu_anh] = lst_moi
    elif choice == "4":
        tu_anh = input("Nhập từ Anh muốn xóa: ").lower()
        if tu_anh in tu_dien:
            del(tu_dien[tu_anh])
            print("Xóa thành công.")
        else:
            print(tu_anh,"không có trong từ điển.")
    elif choice == "0":
        break

