def qlyhanghoa():
    n = int(input("Nhập số lượng mã hàng: "))
    dict_thong_tin = {}
    couts = 0
    while couts < n:
        ma_hang = input("Nhập mã hàng (4 ký tự): ")
        ten_hang = input("Nhập tên hàng: ")
        don_vi = input("Nhập đơn vị tính: ")
        don_gia = float(input("Nhập đơn giá: "))
        so_luong = int(input("Nhập số lượng: "))
        thanh_tien = don_gia * so_luong
        thue = thanh_tien * 0.1
        dict_thong_tin[ma_hang] = [
            ten_hang,
            don_vi,
            don_gia,
            so_luong,
            thanh_tien,
            thue,
        ]
        couts += 1
    sort_dict = sorted(dict_thong_tin.items(), key=lambda x: x[1][5], reverse=True)
    dict_thong_tin_new = {}
    for key, value in sort_dict:
        dict_thong_tin_new[key] = value
    return f"Mặt hàng trước khi sắp xếp là:\n{dict_thong_tin}\nMặt hàng sau khi được sắp xếp là:\n{dict_thong_tin_new}"
