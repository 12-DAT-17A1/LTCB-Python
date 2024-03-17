# Lenh kiem tra so ngay trong mot thang.
month = int(input("Nhap thang: "))
if month == 2:
    print(f"Tháng {month} có thể có 28 hoặc 29 ngày")
elif (month==1)or(month ==3)or(month==5)or(month==7)or(month==8)or(month==10)or(month==12):
    print(f"Thang {month} co 31 ngay")
elif (month==2)or(month ==4)or(month==6)or(month==9)or(month==11):
    print(f"Thang {month} co 30 ngay")
else:
    print("Khong co thang nay trong nam")
