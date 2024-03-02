print("Nhập vào tháng kiểm tra có bao nhiêu ngày trong tháng đó:")
month = int(input("Nhập tháng: "))
if month == 2:
    year = int(input("Nhập năm: "))
    if (month % 4 == 0 and month % 100 != 0) or (month % 400 == 0):
        print(f"Tháng {month} có 29 ngày")
    else:
        print(f"Tháng {month} có 28 ngày")
elif month in (1, 3, 5, 7, 8, 10, 12):
    print(f"Tháng {month} có 31 ngày")
elif month in (2, 4, 6, 9, 11):
    print(f"Tháng {month} có 30 ngày")
else:
    print(f"Không có tháng {month} trong năm")
