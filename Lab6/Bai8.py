n = int(input("Nhập n: "))
lst = [i0 := 0, i1 := 1] + [i1 := i0 + (i0 := i1) for _ in range(2, n + 1)]
print(lst)
