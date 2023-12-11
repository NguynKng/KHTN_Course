while True:
    n = int(input("Nhap n: "))
    if n < 2:
        print("Nhap sai, nhap lai!")
    else:
        break

if n==2:
    print(f"{n} la so nguyen to")
else:
    for i in range(2,n):
        if n % i == 0:
            print(f"{n} khong phai la so nguyen to")
            break
    else:
        print(f"{n} la so nguyen to")