chu_vi = lambda x,y: (x+y)*2
dien_tich = lambda x,y: x*y
while True:
    x,y = eval(input("Nhap x va y: "))
    if x > 0 and y > 0:
        break
print("Chu vi hinh chu nhat la",chu_vi(x,y))
print("Dien tich hinh chu nhat la",dien_tich(x,y))