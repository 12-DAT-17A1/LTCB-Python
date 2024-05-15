try:
       a = int(input("Nhập cạnh a: "))
       b = int(input("Nhập cạnh b: "))
       c = int(input("Nhập cạnh c: "))
       if str(a).isalpha() or str(b).isalpha() or str(c).isalpha():
              raise ValueError("Lõi do có một cạnh nhập vào không phải kiểu số")
       elif a<=0 or b<=0 or c<=0:
              raise ValueError("Lỗi có một cạnh nhập vào âm hoặc bằng không")
       elif a+b<c or a+c<b or c+b<a:
              raise ValueError("Lỗi do không tồn tại tam giác với ba cạnh được nhập vào.")
except ValueError as er:
       print(er)
else:
       print("Không có lỗi nào xuất hiện.")