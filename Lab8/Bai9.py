def pheptinh(a, b):
    tong = a + b
    hieu = a - b
    tich = a * b
    if a != 0:
        thuong = a / b
    else:
        thuong = b / a
    return tong, hieu, tich, thuong


a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print(f"Các phép toán vói hai số {a} và {b} là:")
print(
    f"Tổng: {pheptinh(a,b)[0]}\nHiểu: {pheptinh(a,b)[1]}\nTich: {pheptinh(a,b)[2]}\nThuong: {pheptinh(a,b)[3]}"
)
