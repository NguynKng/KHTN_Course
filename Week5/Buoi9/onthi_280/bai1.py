def lst_uoc(n):
    lst = []
    for i in range(1,n):
        if n%i==0:
            lst.append(i)
    return lst
def so_hua_hon(a,b):
    if (sum(lst_uoc(a))-b==1) or (sum(lst_uoc(b))-a==1):
        return True
    else:
        return False
a,b = eval(input("Nhap 2 so a va b: "))
if so_hua_hon(a,b):
    print(f"{a} va {b} la 2 so hua hon.")
else:
    print(f"{a} va {b} khong la 2 so hua hon.")