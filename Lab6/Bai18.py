# Tạo ma trận kích cỡ m x n:
row = int(input("Mời nhập số hàng: "))
colums = int(input("Mời nhập số cột: "))
lst = [
    [int(input(f"Nhập phần tử thứ {j+1} là: ")) for j in range(colums)]
    for i in range(row)
]
for row in lst:
    for colums in row:
        print("{:<5}".format(colums), end=" ")
    print("\n")
# Tính tổng các phần tử của ma trận trên:
total = 0
for m in lst:
    for n in m:
        total += n
print(f"Tổng các phẩn tử trong ma trận là: {total}")
