a,b = eval(input("Nhập a và b: "))
print(f"Phương trình có dạng: {a}x + {b} = 0")
if a == 0 and b == 0:
    print("Phương trình vô số nghiệm")
elif a == 0 and ( b > 0 or b < 0):
    print("Phương trình vô nghiệm")
else:
    x = -b/a
    print("Vậy x = {}".format(-b/a))
    

