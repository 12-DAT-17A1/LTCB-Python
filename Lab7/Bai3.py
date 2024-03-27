import random

n = int(input("Nhập số phần tử: "))
rally_a = {round(random.uniform(0.0, 10.0), 1) for _ in range(n)}
print(rally_a)
max_number = max(rally_a)
min_number = min(rally_a)
print(f"Phần tử lớn nhất trong tập hợp là: {max_number}")
print(f"Phần tử nhỏ nhất trong tập hợp là: {min_number}")
