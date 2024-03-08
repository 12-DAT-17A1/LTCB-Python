wiedth = int(input("Nhập chiều rộng: "))
length = int(input("Nhập chiều dài: "))
if wiedth != length:
    for i in range(length):
        for j in range(wiedth):
            print("*", end=" ")
        print("\r")
else:
    print("Nhập sai số đo.")
