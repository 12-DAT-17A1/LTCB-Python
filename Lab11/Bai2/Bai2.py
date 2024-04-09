with open("Inp.txt",mode="r",encoding="utf-8") as file_Inp:
       list_dayso = list(map(int,file_Inp.readline().strip().split()))
       list_sort_dayso = sorted(list_dayso)
with open("Out.txt",mode="w") as file_Out:
       write = file_Out.write(" ".join(map(str,list_sort_dayso)))
