def matrixvuong():
    n = int(input("Nhập n: "))
    matrix = [
        [int(input(f"Nhập phần tử thứ {j}: ")) for j in range(1, n + 1)]
        for i in range(n)
    ]
    print(f"Ma trận vuông với kích thước {n}x{n}.")
    for row in matrix:
        for colums in row:
            print("{:<5}".format(colums), end="")
        print()
    list_matrix_chuyen_vi = []
    for i in range(len(matrix)):
        lst = []
        for j in range(len(matrix)):
            lst.append(matrix[j][i])
        list_matrix_chuyen_vi.append(lst)
    print("Ma trận chuyển vị là:")
    for dong in list_matrix_chuyen_vi:
        for cot in dong:
            print("{:<5}".format(cot), end="")
        print()
    if matrix == list_matrix_chuyen_vi:
        return "Đây là ma trận đỗi xứng"
    else:
        return "Đây không là ma trận đối xứng"
