rally_a = set()
while True:
    number = input("Nhap so tu nhien: ")
    if number.isdigit():
        rally_a.add(int(number))
    print("Nhap exit: de thoat.")
    if number == "exit":
        break
print(rally_a)
