flat = True
while flat == True:
    chain = input("Nhập kí tự: ")
    if len(chain) == 1:
        print(ord(chain))
        break
    else:
        print("Vui lòng nhập một kí tự.")
        flat = True
