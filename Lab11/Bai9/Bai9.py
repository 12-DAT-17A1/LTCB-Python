with open("./PASSENGER.IN.txt",mode="r",encoding="utf-8") as file_pass:
       list_chain = file_pass.readlines()
       list_number = [list(map(eval,i.split())) for i in list_chain][1:]
       list_number_total  = [sum(j) for j in list_number]
       list_stt_total = [inx+1 for inx, gt in enumerate(list_number_total) if gt >23]
       list_number_total_chain = [number+"\n" for number in map(str,list_number_total)]
       list_quantity = [len(k) for k in list_number]
       list_stt_quantity = [inx+1 for inx,gt in enumerate(list_quantity) if gt>5]
       list_stt = set(list_stt_quantity) | set(list_stt_total)
       list_stt_false = [chr+"\n" for chr in map(str,list_stt)]
with open("./WEIGHT.OUT.txt",mode="w") as file_weight:
       file_weight.writelines(list_number_total_chain)
with open("./CANCELED.OUT.txt",mode="w") as file_canceled:
       file_canceled.writelines(list_stt_false)