r = int(input("Nhập bán kính: "))
l = int(input("Nhập chiều cao: "))
sxq = 2 * 3.14 * r * l
stp = (2 * 3.14 * r * l) + (2 * 3.14 * r**2)
tt = r**2 * 3.14 * l
print(f"Diện tích xung quanh là: {sxq}")
print(f"Diện tích toàn phần là: {stp}")
print(f"Thể tích là: {tt}")
