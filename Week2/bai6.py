a, b = eval(input("Nhap a va b: "))
min = a
if a<b:
    min = a
else:
    min = b
max = 0
for i in range(1,min+1):
    if a % i == 0 and b % i == 0:
        if i > max:
            max = i
print(f"Uoc chung lon nhat cua {a} va {b} la {max}")