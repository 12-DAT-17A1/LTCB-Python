def is_TamGiac(a, b, c):
    if (a + b > c) and (b + c > a) and (a + c > b):
        return True
    return False


def ChuviTamGiac(a, b, c):
    return a + b + c


def S_TamGiac(a, b, c):
    s = (a + b + c) / 2
    return round((s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)
