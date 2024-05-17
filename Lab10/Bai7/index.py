import sys

sys.path.append("E:\Tincoso-Kì 2\LTCB-Python\Lab10\Bai7\packages_b7")
import packages_b7 as pk7
import random

lst = list(random.choices(range(1, 100), k=100))
print(pk7.dayso(lst))
print(pk7.lietkesonguyento(lst))
print(pk7.lietkesonguyento(lst))
print(pk7.tongsole(lst))
