n = int(input("Mời nhập bậc: "))
lst = [[1 for j in range(n)] for i in range(n)]
for i in lst:
    for j in i:
        print("{:<4}".format(j), end="")
    print("\n")
