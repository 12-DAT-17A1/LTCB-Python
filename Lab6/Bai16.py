x = int(input("Mời nhập giá trị x: "))
y = int(input("Mời nhập giá trị y: "))
lst = [[i * j for j in range(y)] for i in range(x)]
print(lst)
