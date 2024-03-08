# a.
for j in range(100):
    n = int(input("Nhập n: "))
    if n > 0:
        break
    print("Sai rồi n phải lớn hơn 0 mời nhập lại!!")
tong = 0
for i in range(1, n + 1):
    tong += i
print(tong)
# b.
for j in range(100):
    n = int(input("Nhập n: "))
    if n > 0:
        break
    print("Sai rồi n phải lớn hơn 0 mời nhập lại!!")
n = int(input("Nhập n: "))
tong = 0
for i in range(1, n + 1):
    tong += 2 * i + 1
print(tong)
# c.
for j in range(100):
    n = int(input("Nhập n: "))
    if n > 0:
        break
    print("Sai rồi n phải lớn hơn 0 mời nhập lại!!")
n = int(input("Nhập n: "))
tong = 0
for i in range(1, n + 1):
    tong += 2 * n
print(tong)
