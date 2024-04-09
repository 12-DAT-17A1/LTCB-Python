#a
with open("./matrix.txt",mode="r",encoding="utf-8") as file_matrix:
       print(file_matrix.readline())
       file_matrix.readline()
       print(file_matrix.readline())
#b
with open("./matrix.txt",mode="r",encoding="utf-8") as file_matrix:
       list_chain =[" ".join(i.strip().split()) for i in file_matrix.readlines()]
for chr in list_chain:
       print(chr)
#c
def create_matrix():
       with open("./matrix.txt",mode="r",encoding="utf-8") as file_matrix:
              list_chain =[" ".join(i.strip().split()) for i in file_matrix.readlines()]
              list_matrix = [list(map(int,i.split())) for i in list_chain]
              return list_matrix
list_matrix_new = []
for i in create_matrix():
       lst = []
       for j in i:
              if j%2!=0:
                     lst.append(j)
              else:
                     lst.append("0")
       list_matrix_new.append(lst)
list_matrix_new_chain = [" ".join(map(str,i))+"\n" for i in list_matrix_new]
with open("./ODD.txt",mode="w") as file_ood:
       file_ood.writelines(list_matrix_new_chain)