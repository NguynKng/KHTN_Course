thanh_tien = int(input("Nhập số tiền: "))
if thanh_tien > 130000:
    thanh_tien = thanh_tien*0.9
print("Vậy số tiền là {:,}".format(thanh_tien))
