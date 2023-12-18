def tong_uoc(so):
    S = 0
    for i in range(1,so):
        if so%i==0:
            S+=i
    return S
while True:
    num1,num2 = eval(input("Nhap 2 so nguyen duong: "))
    if num1 > 0 and num2 > 0:
        break
if tong_uoc(num1) == num2 and tong_uoc(num2) == num1:
    print(f"{num1} va {num2} la 2 so than thiet.")
else:
    print(f"{num1} va {num2} khong phai la 2 so than thiet")