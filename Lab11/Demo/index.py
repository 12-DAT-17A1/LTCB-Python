import csv
import os

# # Dữ liệu cần ghi
# data = [
#     ["Tên", "Tuổi", "Thành Phố"],
#     ["Alice", 24, "New York"],
#     ["Bob", 30, "London"],
#     ["Charlie", 35, "Paris"],
# ]

# # Tạo và ghi dữ liệu vào tập tin CSV
# with open("people.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
# import csv

# # Dữ liệu mẫu
# data = [
#     ["Tên", "Tuổi", "Thành Phố"],
#     ["Alice", "24", "New York"],
#     ["Bob, the Builder", "30", "London"],
#     ['"Charlie"', "35", "Paris"],
# ]

# with open("people_custom.csv", "w", newline="") as file:
#     writer = csv.writer(file, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     writer.writerows(data)
# import csv

# # Danh sách các dictionary chứa dữ liệu
# data = [
#     {"Tên": "Alice", "Tuổi": 24, "Thành Phố": "New York"},
#     {"Tên": "Bob", "Tuổi": 30, "Thành Phố": "London"},
#     {"Tên": "Charlie", "Tuổi": 35, "Thành Phố": "Paris"},
# ]

# # Tên cột
# fields = ["Tên", "Tuổi", "Thành Phố"]

# with open("people_dict.csv", "w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=fields)

#     # Ghi hàng tiêu đề
#     writer.writeheader()

#     # Ghi từng hàng dữ liệu
#     for row in data:
#         writer.writerow(row)

# lst = ["hello", "world"]

# with open("./filedemo.txt", "w") as file:
#     print(file.writelines(lst))
# file = open("filedemo.txt", "r+")
# file.seek(10)  # Di chuyển đến byte thứ 10 từ đầu tập tin
# print(file.tell())  # In ra 10, xác nhận vị trí hiện tại của con trỏ
# file.seek(, 0)  # Di chuyển đến vị trí thứ ba từ cuối tập tin
# print(file.tell())  # In ra vị trí mới, tùy thuộc vào kích thước tập tin
# file.close()
# with open("./heights.txt", "r") as file_read:
#     list_heights = list(map(float, file_read.read().split(",")))
# list_height = [i * 0.0254 for i in list_heights]
# mean_height = sum(list_height) / len(list_height)
# print(round(mean_height, 2))


# Định nghĩa tên các cột
# fieldnames = ["Name", "Age", "Job"]

# # Dữ liệu để ghi vào tập tin CSV
# rows = [
#     {"Name": "Alice", "Age": 24, "Job": "Engineer"},
#     {"Name": "Bob", "Age": 22, "Job": "Designer"},
#     {"Name": "Charlie", "Age": 28, "Job": "Doctor"},
# ]

# # Mở tập tin CSV để ghi dữ liệu
# with open("example_with_header.csv", "w", newline="") as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     # Ghi tên các cột làm header
#     writer.writeheader()

#     # Ghi dữ liệu
#     writer.writerows(rows)
# with open("./file.csv", mode="w", newline="") as file:
#     name_colums = ["msv", "name", "diem"]
#     writer = csv.DictWriter(file, fieldnames=name_colums)
#     writer.writeheader()
#     csv.writer(file).writerows([[1, 2, 3, 4], [4, 5, 6, 7, 8]])
# lst = [
#     ["1", "2", "3", "4"],
#     ["4", "5", "6", "7", "8"],
#     ["1", "2", "3", "4"],
#     ["4", "5", "6", "7", "8"],
#     ["1", "2", "3", "4"],
#     ["4", "5", "6", "7", "8"],
# ]
# with open("./csvfile.csv", mode="a", newline="") as file:
#     csv.writer(file).writerows(lst)
# with open("./filedemo.txt", mode="r", encoding="utf-8") as file:
#     chain = file.read()
#     chain_new = "Nguyễn Tiến Đạt"
#     position = 10
#     new_content = chain[:position] + chain_new + chain[position - 1 :]
# with open("./filedemo.txt", mode="w") as filewrite:
#     filewrite.write(new_content)


# with open("example_with_header.csv", mode="r", encoding="utf-8") as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)  # Bỏ qua tiêu đề nếu cần
#     for row in csv_reader:
#         print(row)

data = [["Name", "Age"], ["Alice", 24], ["Bob", 22]]

with open("example_with_header.csv", mode="a", encoding="utf-8", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

# Mở file CSV và sử dụng DictReader để đọc file
with open("example.csv", mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Duyệt qua từng hàng dữ liệu
    for row in csv_reader:
        # Mỗi hàng được đọc vào là một dictionary với keys là tên các cột
        # và values là giá trị tương ứng của cột đó trong hàng
        print(row)
        # Ví dụ: Truy cập và in giá trị của cột 'Name' và 'Email'
        print(f"Name: {row['Name']}, Email: {row['Email']}")
fieldnames = ["MSV", "NAME", "AGE"]
list_sinh_vien = [[123, "ĐẠT", 19], [456, "NGHỊ", 19], [789, "DUNG", 19]]
with open("student.csv", mode="w", newline="") as file_student:
    writername = csv.DictWriter(file_student, fieldnames=fieldnames)
    writername.writeheader()
    csv.writer(file_student).writerows(list_sinh_vien)

with open("./student.csv", mode="r", encoding="utf-8") as file_student:
    dict_student = csv.DictReader(file_student)
    for i in dict_student:
        print(f"MSV:{i["MSV"]} NAME:{i["NAME"]} AGE: {i["AGE"]}")
with open("student.csv",mode="r",encoding="utf-8") as file_student:
    read_file = csv.reader(file_student)
    next(read_file)
    print(list(read_file))
with open("./fin.dat", mode="r", encoding="utf-8") as file_fin:
    lst = []
    for i in file_fin:
        lst.append(sum(list(map(int, list(i.replace("\n", "").split(" "))))))
lst_new = [str(i) + "\n" for i in lst]
print(lst_new)
with open("fout.dat", mode="w", encoding="utf-8") as file_fout:
       file_fout.writelines(lst_new)
A = [0, 0.3, 5.8, 12, 15, 8.5, 7.0]
lst = [str(i) + "\n" for i in A]
with open("Dulieu.dat", mode="w", encoding="utf-8") as file_dulieu:
       file_dulieu.writelines(lst)


def write_matrix_to_file(lst, filename):
       with open(filename,mode="w",encoding="utf-8")as file_matrix:
              m = len(lst)
              n = len(lst[0])
              file_matrix.write(f"{m} {n}\n")
              lst_string = [" ".join(map(str,i))+"\n" for i in lst]
              file_matrix.writelines(lst_string)

lst = [[1,2,3],[4,5,6],[7,8,9]]
filename = "matrix.txt"
write_matrix_to_file(lst,filename)
with open("matrix.txt",mode="r",encoding="utf-8") as file_matrix:
       m,n = map(int,file_matrix.readline().strip().split())
       lst = []
       for row in range(m):
              lst_a = list(map(float,file_matrix.readline().strip().split()))
              lst.append(lst_a)
       print(lst)


with open("./Data.txt",mode="r",encoding="utf-8") as file_data:
              list_data = [chr.strip().replace("\n","") for chr in file_data.readlines()]
              list_latinh = [[str for str in chr if str.isalpha()] for chr in list_data]
              list_number = [[number for number in i if number.isdigit()] for i in list_data]
              list_chain_latinh = ["".join(chr)+"\n" for chr in list_latinh]
              list_chain_number =  ["".join(number)+"\n" for number in list_number]
with open("Latinh.txt",mode="w",encoding="utf-8") as file_latinh:
       file_latinh.writelines(list_chain_latinh)
with open("Chuso.txt",mode="w",encoding="utf-8") as file_chuso:
       file_chuso.writelines(list_chain_number)
sinh_vien = {

'001001': {'ten_sv': 'Nguyen Van A', 'gioi_tinh': True, 'nam_sinh': '2000'},

'001002': {'ten_sv': 'Tran Thi B', 'gioi_tinh': False, 'nam_sinh': '2001'},

'001003': {'ten_sv': 'Hoang Tuan C', 'gioi_tinh': True, 'nam_sinh': '2002'},

'001004': {'ten_sv': 'Nguyen Thi D', 'gioi_tinh': False, 'nam_sinh': '2003'}

}
with open("sinhvien.csv",mode="w",encoding="utf-8",newline='') as file_sinh_vien:
       fieldnames = ["ma_sv","ten_sv","gioi_tinh","nam_sinh"]
       writer =csv.DictWriter(file_sinh_vien,fieldnames=fieldnames)
       writer.writeheader()
       for msv,sv in sinh_vien.items():
              csv.writer(file_sinh_vien).writerow([msv,sv['ten_sv'], sv['gioi_tinh'], sv['nam_sinh']])


with open("sinhvien.csv",mode="r",encoding="utf-8") as file_read_sinh_vien:
       read_file_dict = csv.DictReader(file_read_sinh_vien)
       list_thong_tin = []
       for dct in read_file_dict:
              gioi_tinh = "Nam" if dct["gioi_tinh"]=="True" else "Nữ"
              print(f"{dct["ma_sv"]}: {dct["ten_sv"]}, {gioi_tinh}, {dct["nam_sinh"]}")
              list_a = [dct["ma_sv"],dct["ten_sv"],gioi_tinh,int(dct["nam_sinh"])]
              list_thong_tin.append(list_a)
       list_thong_tin_sort = sorted(list_thong_tin,key=lambda x: x[3],reverse=True)
       for row in list_thong_tin_sort:
              print(f"{row[0]} {row[1]} {row[2]} {row[3]}")
