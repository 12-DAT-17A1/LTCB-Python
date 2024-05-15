# def transpose_matrix(matrix):
#     # Số hàng và số cột của ma trận ban đầu
#     rows = len(matrix)
#     cols = len(matrix[0])

#     # Tạo ma trận chuyển vị với số hàng bằng số cột của ma trận ban đầu và ngược lại
#     transpose = [[0 for _ in range(rows)] for _ in range(cols)]

#     # Lặp qua từng phần tử trong ma trận ban đầu và đặt vào vị trí tương ứng trong ma trận chuyển vị
#     for i in range(rows):
#         for j in range(cols):
#             transpose[j][i] = matrix[i][j]

#     return transpose


# # Ví dụ: Tạo ma trận ban đầu
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # In ma trận ban đầu
# print("Ma trận ban đầu:")
# for row in matrix:
#     print(row)

# # Tạo ma trận chuyển vị
# transposed_matrix = transpose_matrix(matrix)


# # In ma trận chuyển vị
# print("\nMa trận chuyển vị:")
# for row in transposed_matrix:
#     print(row)
def matrix_chuyen_vi(matrix):
    quantity_row = len(matrix)
    quantity_column = len(matrix[0])
    matrix_rong = [[0 for i in range(quantity_column)] for j in range(quantity_row)]
    for i in range(quantity_row):
        for j in range(quantity_column):
            matrix_rong[j][i] = matrix[i][j]
    return matrix_rong


def check_matrix_doi_xung(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    else:
        if matrix_chuyen_vi(matrix) == matrix:
            return True
        return False


matrix1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

for row in matrix_chuyen_vi(matrix):
    print(row)
print(check_matrix_doi_xung(matrix1))
