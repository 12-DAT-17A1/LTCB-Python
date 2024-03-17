day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
if (day ==31) and ((month==1)or(month==3)or(month==5)or(month==7)or(month==8)or(month==10)or(month==12)):
    print(f"Ngày {1} Tháng {month+1}")
elif (day ==30) and ((month==2)or(month==4)or(month==6)or(month==9)or(month==11)):
    print(f"Ngày {1} Tháng {month+1}")
elif (day==28)and (month==2):
    print(f"Ngày {1} Tháng {month+1}")
else:
    print(f"Ngày {day+1} Tháng {month}")