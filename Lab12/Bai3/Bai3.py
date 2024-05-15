try:
       filename = input("Nhập tên tập tin: ")
       with open(filename,mode="r",encoding="utf-8") as file_read:
              list_file_read  = file_read.readlines()
       with open("copy.dat","w") as file_copy:
              file_copy.writelines(list_file_read)
except FileNotFoundError as er:
       print("Lỗi do không tìm thấy file:",er)
else:
       print("file đã được copy")