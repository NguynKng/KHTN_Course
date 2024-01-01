users={'user01':['Phan Hoàng Hải Đăng','Abcd@123'],
'user02':['Lưu Minh Phúc','Abcd@123'],
'user03':['Đỗ Thái Minh','Abcd@123']
}
def print_board(dict):
    print("{:20}{:30}{:20}".format("Username","Họ tên","Password"))
    for item in dict:
        thong_tin = dict[item]
        name = thong_tin[0]
        pw = thong_tin[1]
        print("{:20}{:30}{:20}".format(item,name,pw))
def check_upper(password):
    for _char in password:
        if _char.isupper():
            return True
    return False
def check_lower(password):
    for _char in password:
        if _char.islower():
            return True
    return False
def check_number(password):
    for _char in password:
        if _char.isdigit():
            return True
    return False
def check_space(password):
    for _char in password:
        if _char==' ':
            return False
    return True
def check_pass(password):
    if(check_upper(password) and check_lower(password) and check_number(password) and check_space(password) 
        and not password.isalnum() and len(password)>=8
    ):
        return True
    return False
def add_account(_dict):
    username = input("Nhap username: ")
    if username not in _dict:
        name = input("Nhập họ và tên: ")
        pw = input("Nhập password: ")
        if check_pass(pw):
            _dict[username] = [name,pw]
            print("Them thanh cong")
        else:
            print("Password khong hop le.")
    else:
        print("Ten dang nhap khong hop le.")
    return _dict
while True:
    print("CT QUẢN LÝ TÀI KHOẢN.")
    print("1. Xem các tài khoản.")
    print("2. Thêm 1 tài khoản mới.")
    choice = input("Nhap lua chon: ")
    if choice == "1":
        print_board(users)
    elif choice == "2":
        add_account(users)
    else:
        break