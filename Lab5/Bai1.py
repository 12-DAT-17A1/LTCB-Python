# Đếm kí tự số có trong chuỗi.
chain = input("Nhập chuỗi: ")
count_string = 0
for i in chain:
    check = i.isdigit()
    if check:
        count_string += 1
print(count_string)
