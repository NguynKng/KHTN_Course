def IsPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2,n):
            if (n % i) == 0:
                return False
    return True
def dao_chuoi(n):
    chuoi_nguoc = ''
    while n!=0:
        chuoi_nguoc = chuoi_nguoc + str(n%10)
        n = n // 10
    return int(chuoi_nguoc)
def IsEmirp(n):
    if IsPrime(n) and IsPrime(dao_chuoi(n)):
        return True
    else:
        return False
n = int(input("Nhap n: "))
if IsEmirp(n):
    print(f"{n} is EMIRP")
else:
    print(f"{n} is not EMIRP")