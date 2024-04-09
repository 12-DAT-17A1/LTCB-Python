def snt(n):
              if n <2:
                     return False
              for i in range(2,int(n**0.5)+1):
                     if n%i==0:
                            return False
              return True
def check(number,i):
       if number%i==0:
              return True
       return False
       
              
                     
       
with open("f_in.dat",mode="r",encoding="utf-8") as file_in:
       lst = [str.replace("\n","") for str in file_in.readlines()]
       list_number = list(map(int,lst))
list_uoc_so = []
for number in list_number:
       for i in range(2,number):
              if snt(i):
                     if check(number,i):
                            list_uoc_so.append(i)
                            break
       else:
              list_uoc_so.append("No")


list_chain_uoc_so =[number+"\n" for number in map(str,list_uoc_so)]
with open("f_out.dat",mode="w") as file_out:
       file_out.writelines(list_chain_uoc_so)