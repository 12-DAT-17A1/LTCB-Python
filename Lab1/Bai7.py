a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
x_dinh = -b / (2 * a)
y_dinh = a * x_dinh**2 + b * x_dinh + c
x_dinh = round(x_dinh, 2)
y_dinh = round(y_dinh, 2)
print(f"Tọa độ đỉnh parabol là: ({x_dinh}, {y_dinh})")
