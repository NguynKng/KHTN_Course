money = int(input("Số tiền muốn đổi: "))
tien_500 = money//500000 #duoc 1
money = money % 500000
tien_200 = money//200000
money = money % 200000
tien_100 = money//100000
money = money % 100000
tien_50 = money//50000
money = money % 50000
print("Số tờ 500k:",tien_500)
print("Số tờ 200k:",tien_200)
print("Số tờ 100k:",tien_100)
print("Số tờ 50k:",tien_50)
print("Số tiền thừa là:",money)
