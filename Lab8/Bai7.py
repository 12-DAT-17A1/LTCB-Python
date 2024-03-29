def max_and_min(a, b, c):
    max_number = max(a, b, c)
    min_number = min(a, b, c)
    return (max_number, min_number)


a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
print(
    f"Số lớn nhất và nhở nhất trong ba số lần lượt là: {max_and_min(a,b,c)[0]} và {max_and_min(a,b,c)[1]}"
)
