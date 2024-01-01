info = {
    "SV001": ["TOANRR",9.0],
    "SV002": ["TOANCC",5.8],
    "SV003": ["TOANRR",6.5],
    "SV004": ["LAPNC",8.5],
    "SV005": ["TOANCC",4.3]
}
def print_board(dict):
    print("{:15}{:15}{:15}".format("Mã sách","Mã môn","Điểm"))
    for item in dict:
        thong_tin = dict[item]
        ma_mon = thong_tin[0]
        diem = thong_tin[1]
        print("{:15}{:15}{:15}".format(item,ma_mon,str(diem)))
def thong_ke(ma_mon,dict):
    so_luong = 0
    tong_diem = 0
    for item in dict:
        thong_tin = dict[item]
        if ma_mon == thong_tin[0]:
            so_luong +=1
            tong_diem += float(thong_tin[1])
    dtb = tong_diem/so_luong
    print("{:20}{:20}{:20}".format(ma_mon,str(so_luong),str(dtb)))
while True:
    print("--------Chương trình quản lí kết quả học tập sinh viên.")
    print("1. Xem kết quả lưu trữ.")
    print("2. Thống kê.")
    print("0. Thoát")
    choice = input("Nhap lua chon: ")
    if choice == "1":
        print_board(info)
    elif choice == "2":
        lst_ma = set()
        for item in info:
            thong_tin = info[item]
            lst_ma.add(thong_tin[0])
        print("{:20}{:20}{:20}".format("Mã môn","SL","ĐTB"))
        for ma_mon in sorted(lst_ma):
            thong_ke(ma_mon,info)
    elif choice == "0":
        exit()