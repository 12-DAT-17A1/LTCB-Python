str1 = input("Nhap str1: ")
str2 = input("Nhap str2: ")
chain = ""
while True:
    for i in range(len(str1)):
        if len(str1) != 0 or len(str2) != 0:
            chain += str1[0]
            chain += str2[0]
            str1[1:]
            str2[1:]
        else:
            break
    if len(str1) == 0:
        chain += str2
        break
    elif len(str2) == 0:
        chain += str1
        break
    else:
        break
print(chain)
