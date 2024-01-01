def isPangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in string.lower():
            return False
    return True
chuoi = input("Nhap chuoi: ")
if isPangram(chuoi.lower()):
    print("yes")
else:
    print("no")