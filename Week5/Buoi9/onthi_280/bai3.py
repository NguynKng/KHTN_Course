def chuoi_nguoc(chuoi):
    lst_chuoi = list(chuoi)
    lst_chuoi.reverse()
    return ''.join(lst_chuoi)
def chuoi_doi_xung(chuoi):
    if chuoi == chuoi_nguoc(chuoi):
        return True
    else:
        return False
chuoi = input("Nhap chuoi: ")
if chuoi_doi_xung(chuoi):
    print("Chuoi doi xung.")
else:
    print("Khong phai chuoi doi xung.")