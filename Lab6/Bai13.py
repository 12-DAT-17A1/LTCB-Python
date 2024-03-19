lst1 = ["Anh", "Em"]
lst2 = ["Chơi", "Yêu"]
lst3 = ["Bóng  Đá", "Bóng  Rổ"]
lst = [
    "{a1:<5}{a2:<5}{a3:<5}".format(a1=lst1[i], a2=lst2[j], a3=lst3[k])
    for i in range(len(lst1))
    for j in range(len(lst2))
    for k in range(len(lst3))
]
for i in range(len(lst)):
    print(f"{i+1}. {lst[i]}")
