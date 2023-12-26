from libs.function import *
filename = "files/test.txt"
while True:
    print("1. Xem noi dung tap tin.")
    print("2. Ghi de noi dung xuong file.")
    print("3. Them noi dung vao file.")
    print("4. Thong ke file gom bao nhieu dong, tu va ki tu.")
    print("0. Thoat.")
    choice = input("Nhap chuc nang: ")
    if choice == "1":
        print(open_file(filename))
    elif choice == "2":
        write_file(filename)
    elif choice == "3":
        append_file(filename)
    elif choice == "4":
        print("------So dong cua file la {}.".format(dem_dong(filename)))
        print("------So ky tu cua file la {} khong bao gom khoang trang.".format(dem_ky_tu(filename)))
        print("------So tu cua file la {}.".format(dem_tu(filename)))
    elif choice == "0":
        exit()