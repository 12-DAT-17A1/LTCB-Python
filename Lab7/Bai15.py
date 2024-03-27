lst = [1, 2, 3, 4]
lst_name = ["dat", "nghi", "dung", "cuong"]
dict_list = dict()
for index, value in list(enumerate(lst)):#Duyệt qua list chứ các tuple index và phần tử của lst.
    dict_list[value] = lst_name[index] 
print(dict_list)
