def dtb():
    name = input("Nhập tên sinh viên: ")
    diem_toan = float(input("Nhập điểm toán: "))
    diem_ly = float(input("Nhập điểm lý: "))
    diem_hoa = float(input("Nhập điểm hóa: "))
    dtb = (diem_toan + diem_hoa + diem_ly) / 3
    return dtb


print(dtb())
