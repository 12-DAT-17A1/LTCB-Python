a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
kq = a * b
while b:
    a, b = b, a % b
kq /= a
print(kq)
