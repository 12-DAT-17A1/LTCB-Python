max1 = 0
max2 = 0

flat = True
while flat == True:
    n = int(input("Số phần tử nhập vào là: "))
    if n >= 2:
        flat = False
        lst = []
        for i in range(n):
            so = int(input(f"Nhập phần tử thứ {i+1} là: "))
            lst.append(so)
        for j in lst:
            if max1 < j:
                max1 = j
        for k in lst:
            if max2 < k and k != max1:
                max2 = k
        vitri = lst.index(max2)
        print(
            f"Phần tử lớn thứ hai là: {max2}\nVi tri của phần tử lớn thứ hai là: {vitri+1}"
        )
    else:
        flat = True


###
print(lst)
count_number = 0
lst_count = []
for i in lst:
    if i > 0:
        count_number += 1
    else:
        lst_count.append(count_number)
        count_number = 0
lst_count.append(count_number)
print(f"Số lượng các số dương liên tiếp lớn nhất là: {max(lst_count)}")
##
count_number = 0
lst_total = []
for i in lst:
    if i > 0:
        count_number += i
    else:
        lst_total.append(count_number)
        count_number = 0
lst_total.append(count_number)
print(f"Số lượng các số dương liên tiếp có tổng lớn nhất là: {max(lst_total)}")
