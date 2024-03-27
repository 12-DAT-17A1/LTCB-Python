rally = set()
while True:
    characters = input("Nhap ky tu: ")
    if str(characters) == "esc":
        break
    else:
        rally.add(characters)
    print("Nhap esc: de thoat.")
rally_two = set()
for characters in rally:
    if characters.isdigit():
        continue
    else:
        rally_two.add(characters)
print(rally_two)
