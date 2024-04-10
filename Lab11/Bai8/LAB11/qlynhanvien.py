from libs.xu_ly_thong_tin_nhanvien import *

print(F"""
{"MENU".center(80,"*")}
1,Nhập thông tin nhân viên mới.                                                                   
2,In thông tin nhân viên ra màn hình.                                                            
3,Sắp xếp nhân viên giảm dần của thực lĩnh và in ra thông tin được sắp xếp. 
{"END".center(80,"*")}
""")
select = int(input("Mời nhập lựa chọn của bạn: "))
if select==1:
       nhapthongtinnv()
elif select ==2:
       inthongtin()
elif select ==3:
       sapxepthongtin()
else:
       print("Chức năng bạn vừa chọn không có trong MENU.")