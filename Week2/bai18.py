_str = input("Nhập 1 chuỗi bất kỳ: ")
lst_str = _str.split()
set_str = sorted(set(lst_str))
num_word = len(set_str)
num_char = 0
for i in set_str:
    num_char = num_char + len(i)
print(set_str)
print("Số ký tự",num_char)
print("Số từ",num_word)