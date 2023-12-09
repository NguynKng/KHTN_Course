#cach1
print("Cách 1:")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
print("Tổng: ",a+b)
print("Hiệu: ",a-b)
print("Tích: ",a*b)
print("Thương: ",a/b)   
#cach2
print("Cách 2:")
print("Tổng: %.2f"%(a+b))
print("Thương: %.2f"%(a/b))
#cach3
print("Cách 3:")
print("{:.2f} + {:.2f} = {:.2f}".format(a,b,a+b))
print("{:.2f} * {:.2f} = {:.2f}".format(a,b,a*b))