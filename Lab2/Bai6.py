number = int(input("Mời nhập vào số nguyên có ba chữ số: "))
tram =number//100
if (tram==0):
    tram="Không"
elif (tram==1):
    tram= "Một"
elif (tram==2):
    tram= "Hai"
elif (tram==3):
    tram= "Ba"
elif (tram==4):
    tram= "Bốn"
elif (tram==5):
    tram= "Năm"
elif (tram==6):
    tram= "Sáu"
elif (tram==7):
    tram= "Bảy"
elif (tram==8):
    tram= "Tám"
elif (tram==9):
    tram= "Chín"
chuc = number//10
chuc=chuc%10
if (chuc==0):
    chuc="Không"
elif (chuc==1):
    chuc= "Một"
elif (chuc==2):
    chuc= "Hai"
elif (chuc==3):
    chuc= "Ba"
elif (chuc==4):
    chuc= "Bốn"
elif (chuc==5):
    chuc= "Năm"
elif (chuc==6):
    chuc= "Sáu"
elif (chuc==7):
    chuc= "Bảy"
elif (chuc==8):
    chuc= "Tám"
elif (chuc==9):
    chuc= "Chín"
donvi = number%10
if (donvi==0):
    donvi="Không"
elif (donvi==1):
    donvi= "Một"
elif (donvi==2):
    donvi= "Hai"
elif (donvi==3):
    donvi= "Ba"
elif (donvi==4):
    donvi= "Bốn"
elif (donvi==5):
    donvi= "Năm"
elif (donvi==6):
    donvi= "Sáu"
elif (donvi==7):
    donvi= "Bảy"
elif (donvi==8):
    donvi= "Tám"
elif (donvi==9):
    donvi= "Chín"
print(f"{tram} Trăm {chuc} Mươi {donvi}")