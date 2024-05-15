def dayso(n):
       if n<2:
              return 1
       else:
              return n + dayso(n-1)
def daysobinhphuong(n):
       if n<2:
              return 1
       else:
              return n**2 + dayso(n-1)
try:
              n = int(input("Nhập n: "))
              if n<1:
                     raise ValueError("Lỗi do nhập số nhở hơn 1")
except ValueError as er:
              print(er)
else:
       print(dayso(n))
       print(daysobinhphuong(n))