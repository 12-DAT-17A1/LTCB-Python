def number_max(a, b, c):
    def number(x, y):
        if x > y:
            return x
        else:
            return y

    return number(a, number(b, c))


a, b, c = 6, 2, 8
print(number_max(a, b, c))
