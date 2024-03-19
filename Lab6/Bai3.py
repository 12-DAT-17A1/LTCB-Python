lst = []
while True:
    n = int(input("Nhập các phần tử đến khi nhập 0(để dừng): "))
    if n == 0:
        break
    lst.append(n)
###
lst.sort(reverse=True)
print(lst)
###
m = int(input("Nhập phần tử cần chèn là: "))
lst.insert(0, m)
lst.insert(4, m)
lst.append(m)
print(lst)
