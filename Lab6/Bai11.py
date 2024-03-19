import random as rd

n = int(input("Nhập số phần tử: "))
lst = [int(input(f"Nhập phần tử thứ {i+1} là: ")) for i in range(n)]
# Tạo danh sách chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5.
lst_number = [j for j in lst if (j % 3 == 0) and (j % 5 != 0)]
print(
    f"Danh sách các phần tử chia hết cho 3 nhưng không chia hết cho 5 là:\n{lst_number}"
)
# Tạo một danh sách gồm các phần tử bình phương của danh sách ban đầu.
lst_square = [i**2 for i in lst]
print(f"Danh sách các phần tử bình phương của danh sách ban đầu là:\n{lst_square}")
# Tạo một danh sách gồm  các phần tử lấy ngẫu nhiên  từ dnah sách ban đầu mà chia hết cho 3.
lst_s = [i for i in lst if i % 3 == 0]
lst_ = [rd.choice(lst_s) for i in range(len(lst_s))]
print(f"Danh sách tạo ngẫu nhiên từ ds ban đầu và chia hết cho 3 là:\n{lst_}")
