chuoi = input("Nhap chuoi: ")
count = {}
print("{:10}{:10}".format("Kí tự","Tần số"))
for char in chuoi:
    if char in count and char !=" ":
        count[char] += 1
    elif char == " ":
        pass
    else:
        count[char] = 1
for i in (count):
    print("{:10}{:10}".format(i,str(count[i])))