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
