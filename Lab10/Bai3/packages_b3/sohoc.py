def Ucln(a, b):
    while b:
        a, b = b, a % b
    return a


def Bcnn(a, b):
    return (a * b) / Ucln(a, b)


def SumDivisor(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total
