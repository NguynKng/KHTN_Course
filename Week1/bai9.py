x = int(input("Nhập x: "))
S = 1 + x + (pow(x,3)/3) + (pow(x,5)/5)
print(f"S = 1 + {x} + {x}^3/3 + {x}^5/5")
print("S = {:.2f}".format(S))