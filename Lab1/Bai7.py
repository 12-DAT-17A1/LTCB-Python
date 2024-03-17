# Nhập tọa độ các điểm
a_x = float(input("Nhập tọa độ x của điểm A: "))
a_y = float(input("Nhập tọa độ y của điểm A: "))

b_x = float(input("Nhập tọa độ x của điểm B: "))
b_y = float(input("Nhập tọa độ y của điểm B: "))

c_x = float(input("Nhập tọa độ x của điểm C: "))
c_y = float(input("Nhập tọa độ y của điểm C: "))

# Tính tọa độ trọng tâm
x_t = (a_x + b_x + c_x) / 3
y_t = (a_y + b_y + c_y) / 3

# Làm tròn đến chữ số thập phân thứ hai
x_t = round(x_t, 2)
y_t = round(y_t, 2)

# In kết quả
print("Tọa độ trọng tâm của tam giác là:", (x_t, y_t))
