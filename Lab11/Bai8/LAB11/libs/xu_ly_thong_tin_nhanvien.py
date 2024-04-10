import csv
def nhapthongtinnv():
       soluongnv = int(input("Nhập số lượng nhân viên: "))       
       i = 1
       list_thong_tin = []
       while i <=soluongnv:
              print(f"Mời nhâp thông tin nhân viên thứ {i} là:")
              ma_nv = input("Nhập mã nhân viên: ")
              name_nv = input("Nhập tên nhân viên: ")
              chucvu_nv = input("Nhập chức vụ (TP, PP, NV): ").upper()
              hesoluong_nv = float(input("Nhập hệ số lương nhân viên: "))
              luong_nv = hesoluong_nv * 1490000
              dict_chucvu = {'TP':1000000,'PP':700000,'NV':300000}
              phucapcv_nv = dict_chucvu[chucvu_nv]
              thuclinh_nv = luong_nv +phucapcv_nv
              list_tt = [ma_nv,name_nv,chucvu_nv,hesoluong_nv,luong_nv,phucapcv_nv,thuclinh_nv]
              list_thong_tin.append(list_tt)
              i+=1
       with open("../files/ds_nhanvien.csv",mode="w",newline='') as file_nhanvien:
              lst_name = ["Mã NV","Tên NV","Chức Vụ","HS Lương","Lương","Phụ Cấp","Thực Lĩnh"]
              csv.DictWriter(file_nhanvien,fieldnames=lst_name).writeheader()
              csv.writer(file_nhanvien).writerows(list_thong_tin)
def inthongtin():
       with open("./files/ds_nhanvien.csv",mode="r") as file_read:
              list_thong_tin = csv.reader(file_read)
              for row in list_thong_tin:
                     for colums in row:
                            print("{:<14}".format(colums),end="")
                     print()
def sapxepthongtin():
       with open("./files/ds_nhanvien.csv",mode="r") as file_thong_tin:
              list_thong_tin =csv.reader(file_thong_tin)
              name_colums = [["Mã NV","Tên NV","Chức Vụ","HS Lương","Lương","Phụ Cấp","Thực Lĩnh"]]
              next(list_thong_tin)
              list_sort_thong_tin = sorted(list_thong_tin,key=lambda x: x[-1],reverse=True)
       for row in name_colums+list_sort_thong_tin:
              for colums in row:
                     print("{:<14}".format(colums),end="")
              print()              
              