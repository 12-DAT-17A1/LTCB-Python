try:
       with open("index.txt",mode="x",encoding="utf-8") as file_index:
              file_index.write("hello")
except FileExistsError:
       print("Lỗi do tập tin đã tồn tại")