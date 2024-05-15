with open("dayso.dat",mode="r",encoding="utf-8") as file_dayso:
       read_file_dayso = file_dayso.readline().strip().split()
       list_dayso = list(map(int,read_file_dayso))
total = 0
print(list_dayso)
for i in list_dayso:
       print(i,end=" ")
       if i%2!=0:
              total+=i
print("\n")
print(f"Tổng các số hạng lẻ trong dãy là: {total}")