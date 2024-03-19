user_name = input("Mời nhập tên người dùng: ")
password = input("Nhập pass: ").split(",")
list_accect = []
for mk in password:
    kt1, kt2, kt3, kt4, kt5 = 0, 0, 0, 0, 0
    for i in mk:
        if "a" <= i <= "z":
            kt1 += 1
        if "0" <= i <= "9":
            kt2 += 1
        if i in ["@", "#", "$"]:
            kt3 += 1
        if "A" <= i <= "Z":
            kt4 += 1
    if 6 <= len(mk) <= 12:
        kt5 += 1
    if (kt1 >= 1) and (kt2 >= 1) and (kt3 >= 1) and (kt4 >= 1) and (kt5 >= 1):
        list_accect.append(mk)
print("MK Hợp Lệ:")
for i in list_accect:
    print(i)
