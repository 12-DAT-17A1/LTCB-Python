t_giay = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
P = 220 * 2.7
W = P * t_giay
kWh = W / 1000 / 3600
tien_dien = kWh * 7000
print("Tiền điện phải trả là:", tien_dien, "đồng")
