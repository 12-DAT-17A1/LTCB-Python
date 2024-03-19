lst = []
while True:
    n = int(input("Nhập các phần tử, nhập số 0(dừng lại): "))
    if n == 0:
        break
    lst.append(n)
###
lst2 = lst.copy()
lst2.insert(0, [1, 2, 3])
lst2.insert(4, [1, 2, 3])
lst2.append([1, 2, 3])
print(lst2)
###
k = int(input("Nhập vị trí cần xóa: "))
lst.pop(k - 1)
print(lst)
###
lst.sort()
print(f"List tăng: {lst}")
lst.sort(reverse=True)
print(f"List giảm: {lst}")
