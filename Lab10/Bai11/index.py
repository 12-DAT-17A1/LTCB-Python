import sys

sys.path.append("E:\Tincoso-Kì 2\LTCB-Python\Lab10\Bai11\doicoso")
import doicoso as ds

print(ds.enter_number(2345))
# Chuyển từ hệ thập phân sang các hệ nhị phân, bát phân, thập lục phân.
print(ds.henhiphan(36))
print(ds.hebatphan(254))
print(ds.hethaplucphan(234))
number_chain = input("Nhập chuỗi số: ")
print(ds.nhanbietso(ds.clearchain(number_chain)))
