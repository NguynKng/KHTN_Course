alice = int(input("Số kẹo của Alice: "))
bob = int(input("Số kẹo của Bob: "))
carol = int(input("Số kẹo của Carol: "))
so_keo_huy = (alice + bob + carol) % 3
print(f"Số kẹo cần hủy là {so_keo_huy}")