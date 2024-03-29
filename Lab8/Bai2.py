def ucln(a, b):
    while b:
        a, b = b, a % b
    return a


tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))
print(
    f"Tử và mẫu số sau khi rút gọn là: {tu_so/ucln(tu_so,mau_so)} và {mau_so/ucln(tu_so,mau_so)}"
)
