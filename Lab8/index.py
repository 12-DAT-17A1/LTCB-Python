# def describe_pet(animal, name):
#     print(f"I have a {animal} named {name}.")


# describe_pet(name="Harry", animal="hamster")
def my_function(*args):
    for arg in args:
        print(arg)


# my_function(3, 4, 6, "dat")


def my_functions(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# my_functions(name="dat", age=2005)


def my_function_two(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# my_function_two("minh", age=2005)
def multiply(a, b):
    """
    Return the product of two numbers a and b.
    """
    return a * b


def outer_function(text):
    def inner_function():
        return text.upper()

    return inner_function()


# print(outer_function("nguyen tien dat"))
####Hàm lambda(), map(), filter().
lst = [1, 2, 3, 0]
# print(list(map(lambda x: x + 10, lst)))
# print(list(filter(lambda x: x > 1, lst)))
sort_number = sorted(lst, key=lambda x: -x)
# print(sort_number)


## Lambda and closure.
def power(exponent):
    return lambda base: base**exponent


# square = power(2)
# print(square(3))  # Output: 9
###########################################################
##Hàm reduce.
from functools import reduce

number = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, number)
# print(result) #Kết quả là: 15
# Cung cấp giá trị khởi tạo ban đầu.
result_number = reduce(lambda x, y: x + y, number, 5)
# print(result_number)  # Kết quả là: 20

# Tìm giá trị lớn nhất trong danh sách
max_value = reduce(lambda x, y: x if x > y else y, number)
print(max_value)  # Output: 5

n = 5
factorial = reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial)  # Output: 120


def fibonacci(n):
    return reduce(lambda x, _: x + [x[-2] + x[-1]], range(n - 2), [0, 1])


n = 10
fib_sequence = fibonacci(n)
sum_of_fib = sum(fib_sequence)
print(sum_of_fib)  # Output: 88


words = ["Hàm", "reduce()", "trong", "Python"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(sentence)  # Output: "Hàm reduce() trong Python"
from collections import Counter

list_of_elements = ["a", "b", "a", "c", "b", "a", "b", "b"]
count = Counter(list_of_elements)
most_common = reduce(lambda x, y: x if count[x] > count[y] else y, count)
print(most_common)  # Output: 'b'


coefficients = [1, 2, 3]  # 1x^2 + 2x + 3
x = 2
polynomial_value = reduce(lambda acc, coeff: acc * x + coeff, coefficients[::-1])
print(polynomial_value)  # Output: 11 for 1*(2^2) + 2*2 + 3
##############################################################
# Hàm lambda().
data = [
    {"name": "Tom", "age": 25, "salary": 9000},
    {"name": "Jane", "age": 22, "salary": 7000},
    {"name": "Max", "age": 25, "salary": 8000},
]

# Sắp xếp theo tuổi, sau đó theo mức lương
sorted_data = sorted(data, key=lambda x: (x["age"], x["salary"]))
# print(sorted_data)
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Tính tổng bình phương của các số chẵn
sum_of_squares = reduce(
    lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
)
print(sum_of_squares)
# Hàm `lambda` trả về một hàm `lambda` khác
multiplier = lambda x: lambda y: x * y
doubler = multiplier(2)
tripler = multiplier(3)

print(doubler(5))  # 10
print(tripler(5))  # 15


def safe_operation(func):
    def safe_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return e

    return lambda *args, **kwargs: safe_func(*args, **kwargs)


# Sử dụng hàm trên
safe_divide = safe_operation(lambda x, y: x / y)
print(safe_divide(10, 0))  # phản hồi một ngoại lệ thay vì crash

condition = False
print((lambda: "True Result", lambda: "False Result")[condition]())

#################################################################
# Hàm map().
matrix = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
]

# Tăng mỗi số lên 1
incremented_matrix = list(map(lambda row: tuple(map(lambda x: x + 1, row)), matrix))
print(incremented_matrix)


# Đưa ra bình phương và căn bậc hai của các số
numbers = [1, 4, 9, 16]
results = map(lambda x: (x**0.5, x**2), numbers)
print(list(results))

# Chuyển đổi list các số dạng string sang integer
str_numbers = ["1", "2", "3", "4"]
int_numbers = list(map(int, str_numbers))
print(int_numbers)

# Tính tổng các số tương ứng từ hai lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sums = list(map(lambda x, y: x + y, list1, list2))
print(sums)

# Lọc các số chẵn và trả về bình phương của chúng
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_squares = map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
print(list(even_squares))


#################################################################
# Hàm filter(),
# Lọc các số nguyên tố trong một khoảng
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


primes = filter(is_prime, range(1, 50))
print(list(primes))

from functools import reduce

# Tìm tổng bình phương của các số chẵn
numbers = [1, 2, 3, 4, 5, 6]
even_squares_sum = reduce(
    lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
)
print(even_squares_sum)

# Lọc tất cả các chuỗi từ một list chứa heterogeneous types
mixed_list = ["hello", 100, 23.5, "world", True]
strings = filter(lambda x: isinstance(x, str), mixed_list)
print(list(strings))


# Tách số dương, số âm và số 0
numbers = [0, 1, -1, 2, -2, 3, -3]

positives = filter(lambda x: x > 0, numbers)
negatives = filter(lambda x: x < 0, numbers)
zeros = filter(lambda x: x == 0, numbers)

print("Positives:", list(positives))
print("Negatives:", list(negatives))
print("Zeros:", list(zeros))
####

text = "This is a sample sentence, with a set of words!"
unwanted_chars = ",.!"

# Loại bỏ các ký tự không mong muốn và chuyển đổi tất cả các từ thành chữ thường
cleaned_words = filter(
    None, [word.strip(unwanted_chars).lower() for word in text.split()]
)
print(" ".join(list(cleaned_words)))
