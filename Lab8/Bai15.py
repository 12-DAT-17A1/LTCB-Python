n = int(input("Nhập số lượng phần tử trong list là: "))
list_number = list(
    map(
        lambda x: x**2,
        filter(
            lambda x: x % 2 != 0,
            [int(input(f"Nhập phần tử thứ {i}: ")) for i in range(1, n + 1)],
        ),
    )
)
print(list_number)
