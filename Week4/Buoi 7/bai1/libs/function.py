def open_file(filename):
    f = open(filename,"r",encoding="utf8")
    content = f.read()
    f.close()
    return content

def write_file(filename):
    f = open(filename,"w",encoding="utf8")
    text = input("Nhap noi dung: ")
    f.write(text)
    f.close()

def append_file(filename):
    f = open(filename,"a",encoding="utf8")
    text = input("Nhap noi dung: ")
    f.write(text)
    f.close()

def dem_dong(filename):
    f = open(filename,"r",encoding="utf8")
    so_dong = len([line for line in f.readlines() if line != ''])
    return so_dong

def dem_tu(filename):
    f = open(filename,"r",encoding="utf8")
    so_tu = len(f.read().split(" "))
    return so_tu

def dem_ky_tu(filename):
    f = open(filename,"r",encoding="utf8")
    so_ky_tu = len([line for line in f.read() if line != " "])
    return so_ky_tu