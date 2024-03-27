import random

while True:
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    rally_five_random = set(random.choices(lst, k=5))
    if len(rally_five_random) == 5:
        break

print("Tập hợp gồm 5 phần tử ngẫu nhiên của lst là:", rally_five_random)
