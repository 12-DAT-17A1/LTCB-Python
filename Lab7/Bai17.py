dict_sinh_vien = dict()
quantity = int(input("Nhập số lượng sinh viên: "))
start = 1
while start <= quantity:
    check_msv = False
    check_diem_so = False
    print(f"Nhập thông tin sinh viên thứ {start}:")
    while True:
        msv = input("Nhập msv(6 kí tự số): ")
        name = input("Nhập tên sinh viên: ")
        diem = round(float(input("Nhập điểm (0 - 10): ")))
        if len(msv) == 6 and msv.isdigit():
            check_msv = True
        if (diem >= 0) and (diem <= 10):
            check_diem_so = True
        if check_msv == True and check_diem_so == True:
            dict_sinh_vien[msv] = [name, diem]
            break
        else:
            print("Thông tin trên bạn đã nhập sai định dạng mời nhập lại.")
            print(f"Nhập lại thông tin sv thứ {start}:")
    start += 1
dict_sort_diem = dict(
    sorted(dict_sinh_vien.items(), key=lambda x: x[1][1], reverse=True)
)
print(dict_sort_diem)
