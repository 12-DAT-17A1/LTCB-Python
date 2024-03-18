from math import log2

x = float(input("Nhập x: "))
kq = round((log2(x) / 2) + (1 / log2(x)), 2)
print(kq)


