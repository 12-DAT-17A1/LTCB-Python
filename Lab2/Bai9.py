number = int(input("Nhập số điện: "))
price1,price2,price3,price4 = 2000,2500,3000,5000
if 0<= number <=100:
    tien = number*price1
elif 100< number <=200:
    tien = 100*price1 + (number-100)*price2
elif 200< number <=300:
    tien = 100*price1 + 100*price2 +(number-200)*price3
else:
    tien = 100*price1 +100*price2 +200*price3 +(number-300)*price4
print("Số tiền phải trả là:",tien)