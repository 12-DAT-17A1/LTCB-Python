# SyntaxError: Lỗi này xảy ra khi Python phát hiện ra cú pháp không hợp lệ trong mã nguồn.
# try:
#        print("nguyentiendat");print("true"
# except SyntaxError:
#        print("Lỗi do sai cú pháp")
# IndentationError: Đây là lỗi phổ biến khi không tuân thủ đúng quy tắc thụt lề (indentation) của Python.
# try:
#        if True:
#        print("lỗi")
# except IndentationError:
#        print("Lỗi do không thụt lề")
# NameError: Xảy ra khi biến hoặc tên được sử dụng không được định nghĩa.
# try:
#        print(name)
# except NameError:
#        print("Lỗi do biến không được định nghĩa")
# TypeError: Thường xảy ra khi có sự không phù hợp kiểu dữ liệu trong phép toán hoặc chuyển đổi kiểu dữ liệu không hợp lệ.
# try:
#        print(4+"dat")
# except TypeError:
#        print("Lỗi kiểu dữ liệu")
# ValueError: Được ném khi một hàm nhận đối số có kiểu đúng nhưng giá trị không hợp lệ.
# try:
#        number  = int(input("Nhập số nguyên: "))
# except ValueError:
#        print("Sai kiểu dữ liệu nhập vào.")
# IndexError: Xảy ra khi cố gắng truy cập một chỉ mục trong một danh sách (list) hoặc chuỗi (string) vượt quá giới hạn.
# try:
#        lst = [1,2,3]
#        print(lst[3])
# except IndexError:
#        print("Lỗi index không đúng.")
# KeyError: Tương tự như IndexError, nhưng xảy ra khi cố gắng truy cập một khóa không tồn tại trong từ điển (dictionary).
# try:
#        dct = {}
#        print(dct["dat"])
# except KeyError:
#        print("Lỗi do không tồn tại key trong dict.")

# FileNotFoundError: Thường xảy ra khi cố gắng mở hoặc thực hiện các thao tác trên một tệp không tồn tại.
# try:
#        with open("abc.txt",mode="r",encoding="utf-8") as file:
#               print(file.read())
# except FileNotFoundError:
#        print("Lỗi do cố truy cập file không tồn tại.")
# IOError: Lỗi này có thể xảy ra khi có các vấn đề về I/O như mất kết nối.
# try:
#        with open("abc.txt",mode="r") as file:
#               print(file.read())
# except IOError:
#        print("Lỗi do không try cập đc file.")
# KeyboardInterrupt: Xảy ra khi người dùng nhấn Ctrl+C để ngắt quá trình thực thi của chương trình.
# try:
#        n  = int(input("Nhập: "))
#        while True:
#               print("dat")
# except KeyboardInterrupt:
#        print("Lỗi do nhập tổ hợp phím Ctrl + C")
# ImportError: Xảy ra khi có lỗi trong quá trình nhập các module, ví dụ như module không tồn tại.
# try:
#        import matplotlib
# except ImportError:
#        print("Lỗi không tìm thấy thư viện.")
# AttributeError: Xảy ra khi cố gắng truy cập một thuộc tính hoặc phương thức không tồn tại của một đối tượng.

# RuntimeError: Lỗi này xuất hiện khi có một lỗi runtime không xác định.

# ZeroDivisionError: Xảy ra khi cố gắng chia một số cho số không.

# MemoryError: Xảy ra khi không đủ bộ nhớ để thực hiện một hoạt động nào đó.

# OverflowError và UnderflowError: Xảy ra khi giá trị quá lớn hoặc quá nhỏ để được biểu diễn bởi kiểu dữ liệu số nguyên.
# try:
#        n = 2**1000000
#        print(n)
# except OverflowError as er:
#        print("Lỗi do số quá lớn không thể biểu diễn.",er)
# ArithmeticError: Là lớp cơ sở cho các ngoại lệ liên quan đến phép toán số học
# try:
#     # Cố gắng thực hiện phép chia cho 0
#     result = 10 / 0
#     print("Kết quả của phép tính là:", result)
# except ArithmeticError as e:
#     print("Đã xảy ra lỗi ArithmeticError:", e)
a = 5
assert a>10,"5 không lớn hơn 10"