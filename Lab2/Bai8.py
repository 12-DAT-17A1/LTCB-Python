tnct = int(input("Nhap TNCT: "))
lcb = 1350000
if tnct<12:
    luong = lcb*2.34
    print("Lương:",luong)
elif 12<=tnct <36:
    luong =lcb*3.33
    print("Lương:",luong)
elif 36<=tnct<60:
    luong = lcb * 3.66
    print("Lương:",luong)
else:
    luong = lcb *3.99
    print("Lương:",luong)