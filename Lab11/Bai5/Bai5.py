with open("./Sbd_Ph.dat",mode="r",encoding="utf-8") as file_sbd:
       list_file_sbd = [list(map(int,i.replace("\n","").split())) for i in file_sbd.readlines()]
with open("./SBD_Ten.txt",mode="r",encoding="utf-8") as file_ten:
       list_file_ten = [i.replace("\n","").split(" ",1) for i in file_ten.readlines()]
with open("./Phieu_Diem.txt",mode="r",encoding="utf-8") as file_diem:
       list_file_diem = [list(map(int,i.replace("\n","").split())) for i in file_diem.readlines()]
list_file_ket_qua=[]
for i in range(len(list_file_sbd)):
       print(f"SBD: {list_file_sbd[i][0]}, TÊN: {list_file_ten[i][1]}, ĐIỂM: {list_file_diem[i][1]}")
       list_file_ket_qua.append([list_file_sbd[i][0],list_file_ten[i][1],list_file_diem[i][1]])
list_sort = sorted(list_file_ket_qua,key=lambda x: x[2])
list_chain = [list(map(str,i)) for i in list_sort]
list_sort_file_ket_qua = [" ".join(i)+"\n" for i in list_chain]
with open("./Ketqua.txt",mode="w") as file_ket_qua:
       file_ket_qua.writelines(list_sort_file_ket_qua)
       