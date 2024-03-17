number = float(input("Nhập điểm: "))
if 0.0<= number <=3.0:
    print("Loại Kém")
elif 3.0 < number <=4.0:
    print("Loại Yếu")
elif 5.0 < number <=6.0:
    print("Loại Trung Bình")
elif 7.0 < number <=8.0:
    print("Loại Khá")
elif 8.0 < number <=9.0:
    print("Loại Giỏi")
else:
    print("Loại Xuất Sắc")