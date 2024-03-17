n = int(input("Nhập số lần tung xúc sắc: "))
p_khong_ra_6 = (5 / 6) ** (3 * n)
p_it_nhat_mot_lan_ra_6 = 1 - p_khong_ra_6
p_it_nhat_mot_lan_ra_6 = round(p_it_nhat_mot_lan_ra_6, 2)
print("Xác suất có ít nhất một lần ra 6 là:", p_it_nhat_mot_lan_ra_6)
