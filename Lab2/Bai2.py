print("Nhập vào các hệ số a,b,c và in ra nghiệm của phương trình bậc hai:")
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
if a != 0:
    delta = b * b - 4 * a * c
    if delta > 0:
        print("Phương trình có hai nghiệm phân biệt:")
        x1 = (-b + delta**0.5) / (2 * a)
        x2 = (-b - delta**0.5) / (2 * a)
        print(f"x1 = {x1:.2f} ")
        print(f"x2 = {x2:.2f} ")
    elif delta == 0:
        print("Phương trình có nghiệm kép x1=x2:")
        x = -b / (2 * a)
        print(f"x = {x:.2f}")
    else:
        print("Phương trình vô nghiệm")
else:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print("Phương trình có nghiệm là", -c / b)
