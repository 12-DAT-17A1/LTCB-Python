flat = True
while flat == True:
    print("MENU".center(30, "*"))
    print("*" + "1,Cafe".center(28, " ") + "*")
    print("*" + "2,Cam Vắt".center(28, " ") + "*")
    print("*" + "3,Nước ép cà rốt".center(28, " ") + "*")
    print("*" + "4,Nước lọc".center(28, " ") + "*")
    print("*" + "5,Nước dừa".center(28, " ") + "*")
    print("*" * 30)
    n = int(input("Mời nhập số: "))
    if n == 1:
        print("Bạn đã chọn Cafe")
        break
    elif n == 2:
        print("Bạn đã chọn Cam Vắt")
        break
    elif n == 3:
        print("Bạn đã chọn Nước Ép Cà Rốt")
        break
    elif n == 4:
        print("Bạn đã chọn Nước Lọc")
        break
    elif n == 5:
        print("Bạn đã chọn Nước Dừa")
        break
    else:
        print("Khong co so trong MENU")
        print("Mời nhập lại.")
