animal_list = ["tiger","monkey","lion","Eagle","Eagle"]
input = input("Nhap con vat ban muon tim so luong: ").lower()
if input in animal_list:
    print(f"{input} xuat hien {animal_list.count(input)} lan")
else:
    print("Con vat khong tim thay!")