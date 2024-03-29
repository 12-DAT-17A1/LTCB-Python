def chuvi_and_dientich(r):
    chuvi = 2 * 3.14 * r
    dientich = 2 * 3.14 * r**2
    return chuvi, dientich


r = float(input("Nhập bán kính: "))
print(
    f"Chu vi và diện tích hình tròn lần lượt là: {chuvi_and_dientich(r)[0]} và {chuvi_and_dientich(r)[1]}"
)
