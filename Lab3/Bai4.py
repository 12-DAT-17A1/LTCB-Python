n = int(input("Nhap n: "))
if n >= 2:
    for j in range(n + 1):
        if j < 2:
            continue
        for i in range(2, int(j**0.5) + 1):
            if j % i == 0:
                break
        else:
            print(j, end=" ")
