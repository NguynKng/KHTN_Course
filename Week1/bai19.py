loai_xe = (input("Nhập loại xe: "))
if loai_xe == "4" and loai_xe == "7":
    print("Nhap xe khong hop le")
else:
    so_km = float(input("Nhap so km di chuyen: "))
    time_cho = int(input("Thời gian chờ: "))
    if loai_xe == "4":
        if 0<so_km<=0.5:
            tien = 11000
        elif 0.5<so_km<=30:
            tien = 11000 + ((so_km-0.5)*17600)
        else:
            tien = 11000 + 29.5*17600 + ((so_km-30)*14500)
    else:
        if 0<so_km<=0.5:
            tien = 12000
        elif 0.5<so_km<=30:
            tien = 11000 + ((so_km-0.5)*19600)
        else:
            tien = 11000 + 29.5*19600 + ((so_km-30)*17100)
    tien_cho = 0
    if time_cho > 5:
        tien_cho = (time_cho-5)*750
    print("Tiền di chuyển: {}".format(tien))
    print("Tiền chờ: {}".format(tien_cho))
    print("Tiền cước: {}".format(tien+tien_cho))
