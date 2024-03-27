n = int(input("Nhập số n: "))
# Cách 1:
dict_number = {i: i**2 for i in range(1, n + 1)}
print(dict_number)
dict_numberone = {}
# Cách 2:
for i in range(1, n + 1):
    dict_numberone[i] = i**2
print(dict_numberone)
