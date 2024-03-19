import random as rd 


number = []#Tạo một list rỗng.
for j in range(0, 201):  # Tạo ra một list gồm các phần tử từ 0 đến 200.
    so = rd.randrange(0, 201)
    number.append(so)
lst = [
    i for i in number if (i % 5 == 0) and (i % 7 == 0)
]  # Tạo một list gồm các số chia hết cho 5 và 7.
random_number = rd.choice(lst)  # Lấy ra một phần tử bất kì có trong lst.
print(f"Số ngẫu nhiên thảo mãn chia hết cho 5 và 7 là: {random_number}")
