chain_number = input("Nhập chuỗi nhị phân chỉ gồm 0 và 1: ")
index_number = 0
total = 0
for chr in chain_number[::-1]:
    if chr == "1":
        total += 2**index_number
    index_number += 1
print(f"Chuỗi sau khi chuyển sang hệ thập phân là: {total}")
