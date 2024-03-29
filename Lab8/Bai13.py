def year():
    year = int(input("Mời nhập năm: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} là năm nhuận.")
    else:
        print(f"{year} không là năm nhuận")


year()


def month():
    month = int(input("Nhập tháng: "))
    if month in (1, 3, 5, 7, 10, 12):
        print(f"Tháng {month} có 31 ngày")
    elif month in (4, 6, 8, 9, 11):
        print(f"Tháng {month} có 30 ngày")
    else:
        year = int(input("Nhập năm: "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"Tháng {month} có 29 ngày")
        else:
            print(f"Tháng {month} có 28 ngày")


month()
