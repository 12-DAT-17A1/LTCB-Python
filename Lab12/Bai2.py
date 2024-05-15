try:
       chain = input("Nhập một chuỗi kí tự: ")
       if chain.isdigit() or chain.isnumeric():
                     raise ValueError("Lỗi chuỗi có chứa một phím không là kí tự.")
       for i in range(len(chain)):
                     if i<len(chain)-4:
                            if (chain[i]*4 == chain[i+1:i+5]):
                                   raise ValueError("lỗi do có kí tự bị lặp lại 5 lần liên tiếp.")
       for i in range(len(chain)):
                     if i<len(chain)-2:
                            if chain[i]*3 ==chain[i+1:i+4]:
                                   raise ValueError("lỗi do có kí tự bị lặp lại 4 lần liên tiếp.")
       for i in range(len(chain)):
                     if i<len(chain)-1:
                            if chain[i]==chain[i+1] :
                                   raise ValueError("lỗi do có kí tự bị lặp lại 2 lần liên tiếp.")
except ValueError as er:
       print("Error:",er)
finally:
       print("Chương trình tiếp tục hoạt đồng.")
