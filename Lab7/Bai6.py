n = int(input("Nhập vào số tự nhiên n: "))
list_element = []
count_number = 3
while len(list_element) != n:
    check = True
    for j in range(2, int(count_number**0.5) + 1):
        if count_number % j == 0:
            check = False
            break
    if check:
        list_element.append(count_number)
    count_number += 1
for i in list_element:
    print(i, end=" ")
