chain = input("Nhập chuỗi: ")
chain_new = ""
for i in chain:
    if ("0" <= i <= "9") or ("A" <= i <= "F") or ("a" <= i <= "f"):
        chain_new += i
tong = 0
hs = 0
for j in range(len(chain_new) - 1, -1, -1):
    if chain_new[j] == "A":
        tong += 10 * (16**hs)
    elif chain_new[j] == "B":
        tong += 11 * (16**hs)
    elif chain_new[j] == "C":
        tong += 12 * (16**hs)
    elif chain_new[j] == "D":
        tong += 13 * (16**hs)
    elif chain_new[j] == "E":
        tong += 14 * (16**hs)
    elif chain_new[j] == "F":
        tong += 15 * (16**hs)
    else:
        tong += int(chain_new[j]) * (16**hs)
    hs += 1
print(
    "Chuỗi sau khi loại bỏ các ký tự không thuộc hệ Hex và chuyển sang thập phân là:",
    tong,
)
