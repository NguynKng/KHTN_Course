#Các hàm
def in_danh_sach(du_lieu):
    stt = 1
    print('{:10}{:15}{:15}'.format("STT",'Username','Password'))
    for k,v in du_lieu.items():
        print('{:10}{:15}{:15}'.format(str(stt),k,v))
        stt +=1
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
def them_tai_khoan(du_lieu):
    username=input('Nhập tên người dùng: ')
    if username in du_lieu:
        print('Tài khoản đã tồn tại.')
    else:
        while True:
            password=input('Nhập mật khẩu: ')
            if check_pass(password):
                du_lieu[username]=password
                print('Thêm thành công!.')
                break
            else:
                print('Mật khẩu chưa đủ mạnh vui lòng nhập lại!.')

def cap_nhat_tk(du_lieu):
    username=input('Nhập tên tài khoản muốn cập nhật: ')
    if username in du_lieu:
        while True:
            pw = input("Nhập mật khẩu cũ: ")
            if pw == du_lieu[username]:
                while True:
                    new_password=input('Nhập mật khẩu mới: ')
                    if new_password == du_lieu[username]:
                        print("Mật khẩu mới trùng với mật khẩu cũ.")
                    else:
                        if check_pass(new_password):
                            du_lieu[username] = new_password
                            print("Cập nhật tài khoản thành công.")
                            break
                        else:
                            print("Mật khẩu mới chưa đúng yêu cầu.")
                break
            else:
                print("Mật khẩu sai, nhập lại.")
    else:
        print("Tài khoản không tồn tại.")

def xoa_tai_khoan(du_lieu):
    username=input('Nhập tên tài khoản bạn muốn xóa: ')
    if username in du_lieu:
        pw = input("Nhập mật khẩu: ")
        if pw == du_lieu[username]:
            del(du_lieu[username])
            print("Xóa tài khoản thành công.")
        else:
            print("Sai mật khẩu.")
    else:
        print("Không tìm thấy tài khoản.")

#Chương trình main
tai_khoan={
    'user01':'abc@123'
}
while True:
    print('CT Quản lý tài khoản')
    print('1. Xem danh sách tài khoản.')
    print('2. Thêm tài khoản.')
    print('3. Cập nhật tài khoản.')
    print('4. Xóa tài khoản.')
    print("0. Thoát.")
    choice=input('Nhập lựa chọn của bạn: ')
    if choice=='1':
        in_danh_sach(tai_khoan)
    elif choice=='2':
        them_tai_khoan(tai_khoan)
    elif choice=='3':
        cap_nhat_tk(tai_khoan)
    elif choice=='4':
        xoa_tai_khoan(tai_khoan)
    elif choice == "0":
        exit()