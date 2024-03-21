n = int(input("Nhập số n: "))
if n > 1:
    kt = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            kt = False
    if kt:
        print(f"{n} là số nguyên tố.")
    else:
        for k in range(n + 1, 2, -1):
            kt = True
            for h in range(2, int(k**0.5) + 1):
                if k % h == 0:
                    kt = False
            if kt:
                print(f"{k} là số nguyên tố gần {n}.")
                break
