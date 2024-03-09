n = int(input("Nhap so: "))
nguyen = n
tong = 0
while nguyen != 0:
    du = nguyen % 10
    nguyen //= 10
    tong += du
print(f"Tong cac chu so cua so {n} la:", tong)
