starttime = int(input("Nhập thời gian bắt đầu: "))
endtime = int(input("Nhập thời gian kết thúc: "))
if 5 <=starttime<=endtime<= 22:
    time = endtime-starttime
    if 11 <=starttime and endtime<=15:
        if 0<time<=3:
            tien = time*100000
        elif 3<time<=17:
            tien= time*75000
        tien = tien-(tien*0.1)
        print(f"Tiền khách thuê sân phải trả là: {tien}")
    else:
        if 0<time<=3:
            tien = time*100000
        elif 3<time<=17:
            tien= time*75000
        print(f"Tiền khách thuê sân phải trả là: {tien}")
else:
    print("Thời gian không hợp lệ")