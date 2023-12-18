from functools import reduce
lst_so = []
while True:
    x = int(input("Nhap phan tu cua mang: "))
    lst_so.append(x)
    choice = input("Nhan 1 de tiep tuc hoac ky tu bat ky de dung lai: ")
    if choice != "1":
        break
print("List ban dau la:",lst_so)
lst_map = list(map(lambda x:x*2,lst_so))
print("List gom cac phan tu co gia tri gap 2 lan:",lst_map)
def check_prime(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
    return True
lst_filter = list(filter(check_prime,lst_so))
print("List gom cac so nguyen to la:",lst_filter)
_reduce = reduce(lambda x,y: x*y,lst_so)
print("Tich cac phan tu trong list la:",_reduce)