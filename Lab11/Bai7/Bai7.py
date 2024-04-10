with open("./m_nums.txt",mode="r",encoding="utf-8") as file_m_nums:
       list_file_m = list(map(int,file_m_nums.readline().strip().split()))
with open("./n_nums.txt",mode="r",encoding="utf-8") as file_n_nums:
       list_file_n = list(map(int,file_n_nums.readline().strip().split()))
list_file_so_chung = []
if len(list_file_m)>len(list_file_n):
       for i in list_file_n:
              if i in list_file_m:
                     list_file_so_chung.append(i)
else:
       for j in list_file_m:
              if j in list_file_n:
                     list_file_so_chung.append(j)
                     
chain_so_chung = " ".join(map(str,list_file_so_chung))
with open("so_chung.txt",mode="w") as file_so_chung:
       file_so_chung.write(chain_so_chung)