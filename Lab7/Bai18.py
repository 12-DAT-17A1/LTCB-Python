dict_sinh_vien = {"001": ["dat", 8], "002": ["nghi", 7], "003": ["dung", 9]}
while True:
    sbd = input("Nhập số báo danh: ")
    if sbd.isdigit():
        if sbd in dict_sinh_vien:
            print(f"Số báo danh {sbd} có thông tin sv là:")
            print(f"Name: {dict_sinh_vien[sbd][0]}.\nĐiểm: {dict_sinh_vien[sbd][1]}.")
            break
        else:
            print(f"Số báo danh {sbd} không có trong danh sách sv.")
            print("Mời nhập thêm thông tin sv mới.")
            name = input("Nhập tên sv: ")
            diem = float(input("Nhập điểm thi sv: "))
            dict_sinh_vien[sbd] = [name, diem]
            print(f"Thông tin đã được update:\n{dict_sinh_vien}")
            break
    else:
        print("Bạn nhập sai định dạng sbd phải là các kí tự số.")
        print("Mời nhập lại.")
