chain = ""
n = int(input("Nhập số: "))
nguyen = n
while nguyen != 0:
    du = nguyen % 10
    nguyen //= 10
    if du == 0:
        chain = "Không " + chain
    elif du == 1:
        chain = "Một " + chain
    elif du == 2:
        chain = "Hai " + chain
    elif du == 3:
        chain = "Ba " + chain
    elif du == 4:
        chain = "Bốn " + chain
    elif du == 5:
        chain = "Năm " + chain
    elif du == 6:
        chain = "Sáu " + chain
    elif du == 7:
        chain = "Bảy " + chain
    elif du == 8:
        chain = "Tám " + chain
    else:
        chain = "Chín " + chain
print(f"Số {n} được đọc là: \n{chain}")
