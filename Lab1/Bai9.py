# Nhập tọa độ điểm M
x = float(input("Nhập tọa độ x của điểm M: "))
y = float(input("Nhập tọa độ y của điểm M: "))
z = float(input("Nhập tọa độ z của điểm M: "))

# Tọa độ điểm đối xứng qua mặt phẳng Oxy
M_oxy = (x, y, -z)

# Tọa độ điểm đối xứng qua mặt phẳng Oxz
M_oxz = (x, -y, z)

# Tọa độ điểm đối xứng qua mặt phẳng Oyz
M_oyz = (-x, y, z)

# In kết quả
print("Tọa độ điểm đối xứng qua Oxy:", M_oxy)
print("Tọa độ điểm đối xứng qua Oxz:", M_oxz)
print("Tọa độ điểm đối xứng qua Oyz:", M_oyz)



