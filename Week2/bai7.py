while True:
    n = int(input("Nhap n: "))
    if n < 0:
        print("Nhap sai, nhap lai")
    else:
        break;
S = 0
for i in range(1,n):
    if n%i==0:
        S = S + i
if S==n:
    print(f"{n} la so hoan hao")
else:
    print(f"{n} khong phai la so hoan hao")