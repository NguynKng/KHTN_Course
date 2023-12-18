def day_CSC(n,d,u):
    lst_CSC = [u]
    for i in range(1,n):
        x = lst_CSC[i-1] + d
        lst_CSC.append(x)
    return lst_CSC
while True:
    u = int(input("Nhap gia tri U0: "))
    d = int(input("Nhap cong sai d: "))
    n = int(input("Nhap n: "))
    if u > 0 and d > 0 and n > 0:
        break
print("Day cap so cong la:",day_CSC(n,d,u))