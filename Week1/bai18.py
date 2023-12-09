import math
a,b,c = eval(input("Nhập a, b, c: "))
print(f"Phương trình có dạng: {a}x^2 + {b}x + {c} = 0")
if (a == 0):
    if b == 0 and c == 0:
        print("Phương trình vô số nghiệm")
    elif b == 0 and ( c > 0 or c < 0):
        print("Phương trình vô nghiệm")
    else:
        x = -c/b
        print("Vậy x = {}".format(-b/a))
else:
    delta = b**2 - (4*a*c)
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        print("Phương trình có nghiệm kép x1 = x2 = {}".format(-b/(2*a)))
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("Phương trình có 2 nghiệm phân biệt: x1 = {}, x2 = {}".format(x1,x2))