with open("f_in.dat",mode="r",encoding="utf-8") as file_in:
       list_dayso = list(map(int,file_in.readline().strip().split()))
list_so_cuc_tri = [];
quantity = 0;
for i in range(1,len(list_dayso)):
       if list_dayso[i-1]< list_dayso[i]>list_dayso[i+1]:
              list_so_cuc_tri.append(list_dayso[i])
              quantity+=1
with open("f_out.dat",mode="w") as file_out:
       chain_cuc_tri = " ".join(map(str,list_so_cuc_tri))
       file_out.write(str(quantity)+"\n")
       file_out.write(chain_cuc_tri)

              