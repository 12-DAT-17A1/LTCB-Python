# n = int(input("Nhập: "))
# kc = 2 * n - 2
# for i in range(0, n):
#     for k in range(kc):
#         print(end=" ")
#     for j in range(0, i + 1):
#         print("*", end=" ")
#     kc -= 2
#     print("\r")

###Tạo hình tam giác cân.
# n = int(input("Nhập: "))
# kc = 2 * n / 2
# for i in range(0, n):
#     for k in range(int(kc)):
#         print(end=" ")
#     for j in range(0, i + 1):
#         print("*", end=" ")
#     kc -= 1
#     print("\r")
# ###Tam giác bằng số.
# n = int(input("Nhập: "))
# num = 1
# for i in range(0, n):
#     for j in range(0, i + 1):
#         print(num, end=" ")
#         num += 1
#     print("\r")
# ###Tam giác bằng chữ cái.
# n = int(input("Nhập: "))
# num = 65
# for i in range(0, n):
#     for j in range(0, i + 1):
#         print(chr(num), end=" ")
#     num += 1
#     print("\r")
# ### Tìm ước chung lớn nhất của hai số.
# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))
# if a > b:
#     gcd = b
# else:
#     gcd = a
# for i in range(1, gcd + 1):
#     if a % i == 0 and b % i == 0:
#         kq = i
# print(f"Ucln của {a} và {b} là: {kq}")
# ###Liệt kê các số nguyên tố có hai chữ số, và tính tổng các số đó.
# tong = 0
# dem = 0
# for i in range(10, 100):
#     kt = True
#     if i < 2:
#         continue
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             kt = False
#             break
#     if kt:
#         tong += i
#         if len(str(i)) == 2:
#             dem += 1
#     else:
#         continue
# print(tong, dem)
# ###Tạo bảng cửu chương.
# n = int(input("Nhập số: "))
# for i in range(1, 11):
#     print(f"{i} x {n} = {i*n}")


###

# # a
# n = int(input("Nhập vào chiều cao của tam giác: "))
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     # In dấu *
#     for j in range(2 * i - 1):
#         if i == 1 or i == n or j == 0 or j == 2 * i - 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# # b
# height = int(input("Nhập chiều cao của tam giác: "))
# # Vòng lặp để in tam giác
# for i in range(height):
#     if i < height - 1:
#         for j in range(height - i - 1):
#             print(" ", end="")
#         for k in range(2 * i + 1):
#             if k == 0 or k == 2 * i:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#     if i == height - 1:
#         for l in range(height):
#             print("*", end=" ")
#     print()

# # c
# n = int(input("Nhập vào chiều cao của tam giác: "))
# for i in range(1, n + 1):
#     for k in range(n - i):
#         print(end=" ")
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()
