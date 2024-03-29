def bcnn(a, b):
    def ucln(a, b):
        while b:
            a, b = b, a % b
        return a

    return (a * b) / ucln(a, b)


a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print(bcnn(a, b))
