n = int(input("Nhập n: "))
tong = 0
for i in range(1, n + 1):
    tong += (2 * i + 2) / (2 * n + 3)
print(round(tong, 3))
