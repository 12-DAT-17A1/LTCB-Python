from functools import reduce

n = int(input("Nhập số nguyên n: "))
total = reduce(
    lambda x, y: x + y, filter(lambda x: x % 2 == 0, [i for i in range(1, n + 1)])
)
print(total)
