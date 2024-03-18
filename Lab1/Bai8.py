a_x = float(input("Nhập tọa độ x của điểm A: "))
a_y = float(input("Nhập tọa độ y của điểm A: "))
b_x = float(input("Nhập tọa độ x của điểm B: "))
b_y = float(input("Nhập tọa độ y của điểm B: "))
c_x = float(input("Nhập tọa độ x của điểm C: "))
c_y = float(input("Nhập tọa độ y của điểm C: "))
x_t = (a_x + b_x + c_x) / 3
y_t = (a_y + b_y + c_y) / 3
x_t = round(x_t, 2)
y_t = round(y_t, 2)
print("Tọa độ trọng tâm của tam giác là:", (x_t, y_t))