str = input("Nhap chuoi: ")
total = 0
number_chain = ""
for i in str:
    if i.isdigit():
        number_chain += i
for j in range(1, int(number_chain)):
    if int(number_chain) % j == 0:
        total += j
if total == int(number_chain):
    print("Chuoi so " + number_chain + " la so hoan hao")
else:
    print("Chuoi so " + number_chain + " khong la so hoan hao")
