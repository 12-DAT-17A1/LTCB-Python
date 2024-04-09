str1 = input("Nhập chuỗi str1: ")
str2 = input("Nhập chuỗi str2: ")
chain = ""
if len(str1) > len(str2):
    for i in str2:
        if i in str1:
            chain += i
        else:

            chain += " "
            continue
else:
    for i in str1:
        if i in str2:
            chain += i
        else:
            chain += " " + i
max_len = 0
chain_new = ""
for chr in chain.split():
    if len(chr) > max_len:
        max_len = len(chr)
        chain_new = chr
print(f"Chuỗi ký tự  con chung của str1 và str2 có độ dài lớn nhất là: {chain_new}")
