while True:
    n = int(input("Nhap n: "))
    if n > 0:
        break
    else:
        print("Nhap so lon hon 0!")
for i in range(2,n+1):
    print(f"Bang cuu chuong {i}")
    for j in range(1,11):
        print(f"{i}x{j}={i*j}",end="\t")
    print("\n")
    