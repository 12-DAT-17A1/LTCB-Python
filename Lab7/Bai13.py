chain = input("Nhập chuỗi kí tự: ")
dict_characters = {}
for i in range(len(chain)):
    count_characters = 0
    for characters in chain:
        if chain[i] == characters:
            count_characters += 1
    dict_characters[chain[i]] = count_characters
print(dict_characters)
