import math
def pascal(n,k):
    return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
while True:
    n = int(input("Nhap n: "))
    if n > 0:
        break
for i in range(0,n+1):
    for j in range(0,i+1):
        print(pascal(i,j),end='\t')
    print("\n")