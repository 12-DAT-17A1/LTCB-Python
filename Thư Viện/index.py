import os

current_dir = os.getcwd()
print("Thư mục làm việc hiện tại:", current_dir)

files_in_dir = os.listdir('.')
print("Các tệp tin và thư mục trong thư mục hiện tại:",files_in_dir)
for item in files_in_dir:
    print(item)

new_dir_path = './new_directory'
os.mkdir(new_dir_path)
print("Đã tạo thư mục mới:", new_dir_path)

# path_to_check = './some_file.txt'
# if os.path.exists(path_to_check):
#     print("Đường dẫn tồn tại.")
# else:
#     print("Đường dẫn không tồn tại.")

# dir_to_delete = './directory_to_delete'
# os.mkdir(dir_to_delete)  # Tạo thư mục để xóa
# os.rmdir(dir_to_delete)
# print("Đã xóa thư mục:", dir_to_delete)

file_path = '/path/to/some/file.txt'
file_name = os.path.basename(file_path)
print("Tên tệp:", file_name)
