m = int(input("Nhập số tự nhiên m: "))
n = int(input("Nhập số tự nhiên n: "))
rally_m = set()
rally_n = set()
nguyen_m = m
nguyen_n = n
while nguyen_m != 0:
    du_m = nguyen_m % 10
    rally_m.add(du_m)
    nguyen_m //= 10
while nguyen_n != 0:
    du_n = nguyen_n % 10
    rally_n.add(du_n)
    nguyen_n //= 10
select = rally_m.intersection(rally_n)
total = 0
for number in select:
    total += number
print(f"Tổng của các chữ số chung là: {total}")
