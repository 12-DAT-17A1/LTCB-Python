# 1. So sánh bằng toán tử:
# ==: Kiểm tra xem hai Set có chứa chính xác các phần tử giống nhau hay không.
# !=: Kiểm tra xem hai Set có khác nhau hay không.
# <: Kiểm tra xem Set thứ nhất có phụ thuộc Set thứ hai hay không (tức là tất cả các phần tử của Set thứ nhất đều thuộc Set thứ hai).
# >: Kiểm tra xem Set thứ nhất có bao gồm Set thứ hai hay không (tức là Set thứ hai là tập con của Set thứ nhất).
# <=: Kiểm tra xem Set thứ nhất có phụ thuộc hoặc bằng Set thứ hai hay không.
# >=: Kiểm tra xem Set thứ nhất có bao gồm hoặc bằng Set thứ hai hay không.
# set1 = {1, 2, 3, 4}
# set2 = {2, 3, 4}
# print(set1 == set2)  # False
# print(set1 != set2)  # True
# print(set1 < set2)  # False
# print(set1 > set2)  # False
# print(set1 <= set2)  # True
# print(set1 >= set2)  # True
# # Các hàm ảnh hưởng đến các phần tử trong set.
# set3 = {"dat", 2, 3, 4, 5, 6, 7}
# set3.pop()
# print(set3)
# value = set3.pop()  # Xóa phần tử ngẫu nhiên.
# print(value)  # Trả về phần tử vừa xóa khỏi set.
# print(set3)
# set3.clear()  # Xóa hết phần tử trong set.
# print(set3)
# lst = [1, 2, 3, 4, "dat"]
# gt = lst.pop(-1)
# print(gt)
# print(lst)
# set4 = {2, 3, 4, 5}
# set4.add("dat")
# set4.add("nghị")
# print(set4)
# set5 = set()
# set5 |= {1, 2, 3, 4, 5}
# print(set5)
# my_dict = dict()

# # Khởi tạo với các cặp khóa-giá trị
# my_dict = dict(name="Bard", age=18)
# print(my_dict)
# name = my_dict.get("name", "unknown")
# age = my_dict.get(
#     "age", "Khóa này không tồn tại"
# )  # Giá trị mặc định nếu khóa không tồn tại
# print(name)
# print(age)
# # Thay đổi giá trị.
# my_dict["age"] = 19
# print(my_dict)
# my_dict.update(name="LaMDA", age=3)
# print(my_dict)
# my_dict["favorite_color"] = "blue"
# my_dict.update({"favorite_food": "pizza"})
# print(my_dict)
# my_dict.pop("name")
# print(my_dict)
# del my_dict["age"]
# print(my_dict)
# del my_dict  # Xóa kiểu dữ liệu my_dict
# my_dict = {"name": "Bard", "age": 2, "favorite_color": "blue"}
# keys = list(my_dict.keys())
# print(keys)  # In ra một list các keys.
# values = list(my_dict.values())
# print(values)  # In ra một list các values.
# items = list(my_dict.items())
# print(items)  # In ra một list các tuple chứa keys và values tương ứng.
# A Python program to demonstrate working of OrderedDict
# from collections import OrderedDict

# print("This is a Dict:\n")
# d = {}
# d["a"] = 1
# d["b"] = 2
# d["c"] = 3
# d["d"] = 4

# for key, value in d.items():
#     print(key, value)

# print("\nThis is an Ordered Dict:\n")
# od = OrderedDict()
# od["a"] = 1
# od["b"] = 2
# od["c"] = 3
# od["d"] = 4
# print(od)
# for key, value in od.items():
#     print(key, value)
# from collections import OrderedDict

# # Create two ordered dictionaries with different orderings
# od1 = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
# od2 = OrderedDict([("c", 3), ("b", 2), ("a", 1)])

# # Compare the ordered dictionaries for equality
# print(od1 == od2)
# from collections import OrderedDict

# dict_ = {"a": 1, "b": 2, "c": 3}
# my_dict = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
# item = my_dict.popitem("a")
# print(item)
# my_dict.move_to_end("a", last=True)
# my_dict.move_to_end("b", last=False)

# print(my_dict)


# for key, value in my_dict.items():
#     print(key, value)
# Python program to demonstrate
# defaultdict


# from collections import defaultdict


# # Function to return a default
# # values for keys that is not
# # present
# def def_value():
#     return "Not Present"


# # Defining the dict
# d = defaultdict(lambda: "không có keys")
# d["a"] = 1
# d["b"] = 2
# print(d["a"])
# print(d["b"])
# print(d["c"])
# ##
# import random
# import math

# a = set(random.choices(range(2, 1001), k=10))
# b = list()
# for number in a:
#     for i in range(2, number + 1):
#         if number % i == 0:
#             is_prime = True
#             for j in range(2, int(math.sqrt(i)) + 1):
#                 if i % j == 0:
#                     is_prime = False
#                     break
#                 if is_prime:
#                     b.append(i)
# print("Tập hợp a:", a)
# print("Tập hợp b:", b)
# d = {"k1601": ["Ha", 7, 9.5], "k1602": ["Binh", 10, 8], "k1603": ["Hoa", 6.0, 9]}
# old = d.copy()
# msv = input("Nhap msv: ")
# content = input("Nhap ten,dhp1,dhp2:  ").split(",")
# if msv in d:
#     d[msv] = [content[0], float(content[1]), float(content[2])]
#     print("Danh sach sau khi cap nhat them:", d)
# else:
#     d[msv] = [content[0], float(content[1]), float(content[2])]
#     print("Danh sach sau khi cap nhat moi mot sv", d)
#     print("Du lieu ban dau la:", old)
# Tính điểm trung bình của các sv.
# d = {"k1601": ["Ha", 7, 9.5], "k1602": ["Binh", 10, 8], "k1603": ["Hoa", 6.0, 9]}
# print("Điểm trung bình học kì 1 là:")
# print("*" * 20)
# for key, value in d.items():
#     dtb = (value[1] + value[2]) / 2
#     print(key, ":")
#     print(value[0], ":", dtb)
#     print("*" * 10)
# DS = {
#     "04": ["Ha", 7],
#     "02": ["Binh", 8],
#     "03": ["Hoa", 9],
#     "05": ["Son", 6],
#     "08": ["Hung", 10],
# }
# GT = {
#     "04": ["Ha", 9],
#     "06": ["Ngoc", 8],
#     "09": ["Van", 7],
#     "05": ["Son", 6],
#     "08": ["Hung", 10],
# }
# TN = {
#     "04": ["Ha", 7],
#     "02": ["Binh", 8],
#     "01": ["An", 9],
#     "05": ["Son", 6],
#     "08": ["Hung", 10],
# }
# DTB = {}
# print("{:<4}{:<6}{:<4}".format("MSV", "TEN", "DTB"))
# for key in DS:
#     if key in GT and key in TN:
#         dtb = (DS[key][1] + GT[key][1] + TN[key][1]) / 3
#         print("{:<4}{:<6}{:<4}".format(key, DS[key][0], round(dtb, 2)))
#         DTB[key] = [key, round(dtb, 2)]
# print("Dữ liệu về điểm trung bình của các sinh viên:")
# print(DTB)
# chain = """ Glucose is the fundamental thing that burns energy in our bodies. We get
# glucose from the foods we eat and it is transmitted to all cells via blood. This way, glucose
# ensures the energy which the cell needs. The quantity of the glucose in our blood shows
# us some data about our body’s health. Measuring blood glucose level is the most common
# way to control people’s medical condition."""
# dl = {}
# chain = chain.split()
# for i in chain:
#     dl[i] = dl.get(i, 0) + 1
# quantity_chain = len(chain)
# print(f"Chuỗi trên có {quantity_chain} từ.")
# for key, value in dl.items():
#     print(key + ":" + str(value), end=", ")
# lst = []
# dl = {}
# while True:
#     msv = input("Nhập msv gồm (4 ký tự) là số: ")
#     if len(msv) == 4 and msv.isdigit():
#         name = input("Nhập họ và tên: ")
#         dhp1 = float(input("Nhập điểm hp1: "))
#         dhp2 = float(input("Nhập điểm hp2: "))
#         dl[msv] = [name, dhp1, dhp2]
#     elif msv == "":
#         break
#     else:
#         print("Bạn nhập sai định dạng msv r nhập lại đi.")
#     print("Nếu muốn thoát ấn Enter.")
# print("{:<8}{:^20}{:>5}{:>5}".format("Mã SV", "Họ tên", "Điểm HP 1", "Điểm HP2"))
# for key, value in dl.items():
#     print("{:<8}{:<20}{:>5}{:>5}".format(key, dl[key][0], dl[key][1], dl[key][2]))
