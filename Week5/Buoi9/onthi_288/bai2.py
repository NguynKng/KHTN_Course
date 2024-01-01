def lucas_lst(n):
    lst = [2,1]
    for i in range(1,n-1):
        lst.append(lst[i]+lst[i-1])
    return lst
n = int(input("Nhap n: "))
print(lucas_lst(n))
chuoi = input("Nhap chuoi: ")
chuoi = list(chuoi)
chuoi.reverse()
chuoi_dao = "".join(chuoi)
print(chuoi_dao)