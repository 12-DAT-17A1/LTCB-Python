import re
try:
       username = input("Enter Username: ")
       for i in username:
              if re.fullmatch(r'[^A-Za-z0-9]+', i):
                     raise ValueError("Lỗi do chứa kí tự đặc biệt.")
except ValueError as er:
       print(er)
else:
       print("Định dạng email chính xác:")
       print(username+"@companyname.com")