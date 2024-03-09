# a
n = int(input("Nhap n: "))
i = 2
tong = 0
while i <= n:
    if i % 2 == 0:
        j = i - 1
        hieu = 0
        while j <= i:
            if j < i:
                hieu += 1 / j
            else:
                hieu += -1 / j
            j += 1
        i += 1
        tong += hieu
    i += 1
print(tong)
# b
flat = True
while flat == True:
    n = int(input("Nhập n: "))
    if n > 1:
        i = 2
        total = 0
        while i <= n:
            j = i - 1
            tich = 1
            while j <= i:
                tich *= 1 / j
                j += 1
            total += tich
            i += 1
        break
    else:
        print("n phai lon hon 1")
        flat = True
print(total)
# c
flat = True
while flat == True:
    n = int(input("nhap n: "))
    if n >= 2:
        i = 2
        total = 0
        while i <= n:
            total += 1 / (i**0.5)
            i += 1
        print(total)
        break
    else:
        print("n phai lon hon 1")
        flat = True
