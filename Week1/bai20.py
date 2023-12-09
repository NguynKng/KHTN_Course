tieu_thu = int(input("Số kilowat tiêu thụ: "))
if tieu_thu <= 50:
    tong_tien = tieu_thu*1678
elif tieu_thu <= 100:
    tong_tien = 50*1678 + ((tieu_thu-50)*1734)
elif tieu_thu <= 200:
    tong_tien = 50*1678 + 50*1734 + ((tieu_thu-100)*2014)
elif tieu_thu <= 300:
    tong_tien = 50*1678 + 50*1734 + 100*2014 + ((tieu_thu-200)*2536)
elif tieu_thu <= 400:
    tong_tien = 50*1678 + 50*1734 + 100*2014 + 100*2536 + ((tieu_thu-300)*2834)
else:
    tong_tien = 50*1678 + 50*1734 + 100*2014 + 100*2536 + 100*2834 + ((tieu_thu-400)*2927)
print("Vậy số tiền phải trả là {:,}".format(tong_tien))
