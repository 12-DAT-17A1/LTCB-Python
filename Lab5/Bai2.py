chain = input("Nhập chuỗi: ")
count_string = 0
for i in chain:
    if i.isalpha() or i.isdigit():
        continue
    else:
        count_string += 1
print(count_string)
