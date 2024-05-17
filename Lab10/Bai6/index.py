import sys

sys.path.append("E:\Tincoso-Kì 2\LTCB-Python\Lab10\Bai6\packages_b6")
import packages_b6 as pk6

chain_number = input("Nhap chuoi so: ")
print(pk6.nhanbietso(pk6.clearchain(chain_number)))
