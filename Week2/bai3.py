A = 0
B = 0
C = 1
D = 1
str_A="A = "
str_B="B = "
str_C="C = "
str_D="D = "
while True:
    n = int(input("Nhap n: "))
    if(n>0):
        break
    else:
        print("Nhap sai, nhap lai")

for i in range (1, n+1):
    C = C*i
    str_C = str_C + str(i) + " x "
    if i%2!=0:
        A = A + i
        str_A = str_A + str(i) + " + "
    if i%2==0:
        B = B + i
        str_B = str_B + str(i) + " + "
    if i%3==0:
        str_D = str_D + str(i) + " x "
        D = D*i
str_A=str_A.rstrip(" + ")+" ="
str_B=str_B.rstrip(" + ")+" ="
str_C=str_C.rstrip(" x ")+" ="
str_D=str_D.rstrip(" x ")+" ="
print(str_A,A)
print(str_B,B)
print(str_C,C)
print(str_D,D)