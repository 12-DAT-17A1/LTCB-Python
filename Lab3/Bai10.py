# a
n = int(input("Nhập vào chiều cao của tam giác: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        if i == 1 or i == n or j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
# b
height = int(input("Nhập chiều cao của tam giác: "))
for i in range(height):
    if i < height - 1:
        for j in range(height - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            if k == 0 or k == 2 * i:
                print("*", end="")
            else:
                print(" ", end="")
    if i == height - 1:
        for l in range(height):
            print("*", end=" ")
    print()

# c
n = int(input("Nhập vào chiều cao của tam giác: "))
for i in range(1, n + 1):
    for k in range(n - i):
        print(end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
