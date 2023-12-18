def fibo(n):
    day_fibo = [0,1]
    for i in range(2,n):
         x = day_fibo[i-2] + day_fibo[i-1]
         day_fibo.append(x)
    return day_fibo
while True:
     n = int(input("Nhap n: "))
     if n > 0:
          break
print(f"Day fibo gom {n} phan tu la",fibo(n))