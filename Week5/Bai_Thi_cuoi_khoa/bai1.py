import calendar
khuyen_mai = 0
ngay_mua = input("Nhap ngay mua hang theo dinh dang dd/mm/yyyy: ")
ngay_mua = ngay_mua.split("/")
list_ngay = "Thứ 2","Thứ 3","Thứ 4","Thứ 5","Thứ 6","Thứ 7","Chủ nhật"
_ngay = int(ngay_mua[0])
_thang = int(ngay_mua[1])
_nam = int(ngay_mua[2])
ten_hang = input("Nhap ten hang: ")
so_luong = int(input("Nhap so luong: "))
don_gia = int(input("Nhap don gia: "))
thanh_tien = so_luong*don_gia
if _ngay == 13 and calendar.weekday(_nam,_thang,_ngay) == 4:
    khuyen_mai = 15/100
giam_gia = thanh_tien*khuyen_mai
print("HOA DON MUA HANG")
print("Thanh tien: {:,} X {} = {:,}".format(don_gia,so_luong,thanh_tien))
print("Giam gia: {:,} VNĐ".format(giam_gia))
print("Thanh toan: {:,} - {:,} = {:,}".format(thanh_tien,giam_gia,round(thanh_tien-giam_gia,2)))
print("Ngay xuat hoa don: {} ngày {}/{}/{}".format(list_ngay[calendar.weekday(_nam,_thang,_ngay)],_ngay,_thang,_nam))