import random
#9.1
while True:
    n = int(input("Nhap n: "))
    if n<0:
        print("Nhap lai")
    else:
        break
A = []
B = []
for i in range(0,n):
    if i%2==0:
        A.append(i)
    else:
        B.append(i)
print("9.1:",A)
#9.2
print("9.2:",B)
#9.3
C = ['Khang','Bin','Tan','Tuyen']
print("9.3: Thanh vien gia dinh bao gom:",'-'.join(C))
#9.4
D = [["SV1","Math",9],["SV2","Math",10],["SV3","Physic",9],["SV1","Biology",7]]
print("Bang diem sinh vien".center(50,"-"))
print("{:10}{:10}{:10}".format("Code","Subject","Point"))
for result in D:
    print("{:10}{:10}{:10}".format(result[0],result[1],str(result[2])))
#9.5
chuoi = input("Nhap chuoi: ")
print("9.5:",chuoi.split())
#9.6
F = []
while True:
    x = input("Nhap phan tu muon them: ")
    F.append(x)
    check = input("Ban co muon nhap them du lieu khong (Yes or No): ").lower()
    if check == "no":
        break
    else:
        continue
print("Vay thong tin ban vua nhap la",end=": ")
for i in F:
    print(i,end=',')