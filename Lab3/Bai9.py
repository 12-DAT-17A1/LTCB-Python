# a.
for j in range(100):
    n = int(input("Nhập n: "))
    if n > 0:
        break
    print("Sai rồi n phải lớn hơn 0 mời nhập lại!!")
tong = 0
for i in range(1, n + 1):
    tong += i**2
print(tong)
# b.
for j in range(100):
    n = int(input("Nhập n: "))
    if n > 0:
        break
    print("Sai rồi n phải lớn hơn 0 mời nhập lại!!")
tong = 0
for i in range(1, n + 1):
    tong += (2 * i + 1) ** 3
print(tong)
# c.
for j in range(100):
    n = int(input("Nhập n: "))
    if n > 0:
        break
    print("Sai rồi n phải lớn hơn 0 mời nhập lại!!")
tong = 0
for j in range(1, n + 1):
    tong += (2 * j) ** 4
print(tong)
