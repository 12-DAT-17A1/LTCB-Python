chain = input("Nhập chuỗi: ")
chain_new = chain.replace(",", "")
for chr in chain_new.split():
    print(chr)
