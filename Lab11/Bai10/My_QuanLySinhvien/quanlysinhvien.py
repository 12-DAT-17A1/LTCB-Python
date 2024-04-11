import csv
def  sinhvien():
       soluong_sv = int(input("Nhập số lượng sinh viên: "))
       list_thong_tin_sv  = []
       for i in range(1,soluong_sv+1):
              print(f"Nhập thông tin sinh viên thứ {i} là:")
              ma_sv = input("Nhập mã sinh viên:")
              name = input("Nhập tên sinh viên: ")
              diem_tb = float(input("Nhập điểm trung bình: "))
              diem_rl = float(input("Nhập điểm rèn luyện: "))
              diem_tl = (diem_tb  + diem_rl)/2
              list_thong_tin_sv.append([ma_sv,name,diem_tb,diem_rl,diem_tl])
       with open("./files/ds_sinhvien.csv",mode="w",newline='') as file_ds:
              name_colums = ["Mã SV","Họ Tên","Điểm TB","Điểm RL","Điểm TL"]
              csv.DictWriter(file_ds,fieldnames=name_colums).writeheader()
              csv.writer(file_ds).writerows(list_thong_tin_sv)
       list_sort_thong_tin =[name_colums]+ sorted(list_thong_tin_sv,key=lambda x: x[3])
       list_thong_tin_sv = [name_colums]+list_thong_tin_sv
       print("Thông tin sinh viên sinh viên trong file ds_sinhvien.csv là:")
       for i in list_thong_tin_sv:
              for j in i:
                     print("{:<10}".format(j),end="")
              print()
       print("Thông tin sinh viên sau khi sắp xếp tăng dần của điểm rèn luyện là:")
       for row in list_sort_thong_tin:
              for colums in row:
                     print("{:<10}".format(colums),end="")
              print()
       max_tl =max(list_sort_thong_tin[1:],key=lambda x: x[4])
       print(f"Thông tin sinh viên có điểm tích lũy cao nhất là:\n{max_tl}")