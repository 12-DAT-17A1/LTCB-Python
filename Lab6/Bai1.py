a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
##
tong = 0
for i in a:
    tong += i
print("Tổng các phần tử trong a là:", tong)
##
dem = 0
tong_duong = 0
for j in a:
    if j > 0:
        dem += 1
        tong_duong += j
print(f"Tổng các số dương là:", tong_duong, f"\nCó {dem} số hạng dương")
##
for k in a:
    if k < 0:
        position = a.index(k)
        break
print(f"Vị trí của phần tử âm đầu tiên là:", position + 1)
##
for p in a:
    if p > 0:
        vitri = a.index(p)
print(f"Vị trí của phần tử dương cuối cùng là: {vitri+1}")
##
max = 0
for so in a:
    if max < so:
        max = so
vitri = a.index(max)
print(f"Phần tử lớn nhất là:{max}\nVi trí phần tử là: {vitri+1} ")
