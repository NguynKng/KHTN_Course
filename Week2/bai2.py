# cau 1
string = input("Nhap 1 chuoi bat ky: ")
for i in range(0,len(string)):
    if string[i] == " ":
        #continue
        print("\nVi tri khoang trang dau tien la: ",i)
        break
    else:
        print(string[i],end=' ')
# cau 2
for i in range(0,len(string)):
    if string[i] == " ":
        continue
    else:
        print(string[i],end=" ")
#cau 3
for i in range(0,len(string)):
    if string[i] == 'a' or string[i]=="A":
        print("\nCo ki tu a")
        break
else:
    print("Khong co ki tu a hay A")