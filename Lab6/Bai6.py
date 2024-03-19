import random as rd

lst = []
for i in range(1000):
    lst.append(rd.randint(1, 99999))
# Cách 1:
print(sorted(lst))
# Cách 2:
for i in range(len(lst)):
    tp = i
    for j in range(i + 1, len(lst)):
        if lst[tp] > lst[j]:
            tp = j
    lst[i], lst[tp] = lst[tp], lst[i]
print(lst)
