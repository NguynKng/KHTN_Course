S = 0
while True:
    x = int(input("Nhap x: "))
    y = int(input("Nhap y: "))
    if (x >=0 and y>=0) and x<y:
        break
    else:
        print("Nhap sai, nhap lai")

for i in range(x,y+1):
    S = S + i**2

print(f"Tong binh phuong tu {x} den {y} la {S}")