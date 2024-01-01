def IsPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2,n):
            if (n % i) == 0:
                return False
    return True
def day_nt(a,b):
    lst = []
    for i in range(a,b+1):
        if IsPrime(i):
            lst.append(i)
    return lst
a,b = eval(input("Nhap pham vi a-b: "))
print(f"Cac so nguyen to trong pham vi tu {a} den {b}:",day_nt(int(a), int(b)))