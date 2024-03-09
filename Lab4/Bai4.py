flat = True
while flat == True:
    ts = int(input("Nhập tử số: "))
    ms = int(input("Nhập mẫu số: "))
    if ms == 0:
        print("Nhập lại do mẫu số = 0")
        flat = True
    else:
        flat = False
