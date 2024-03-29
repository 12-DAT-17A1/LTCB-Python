def uoc_so():
    n = int(input("Nhập số nguyên dương: "))
    if n > 0:
        print(f"Các ước số của {n} là:")
        for i in range(1, n + 1):
            if n % i == 0:
                print(i, end=" ")
    else:
        print("Số vừa nhập ko phải số nguyên dương.")

uoc_so()
