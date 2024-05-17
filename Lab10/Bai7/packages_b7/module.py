import random


def dayso(lst):
    chain = " ".join(list(map(str, lst)))
    return f"Dãy số ngẫu nhiên là:\n{chain}"


def lietkesonguyento(lst):
    # Hàm all trả về false nếu chỉ một điều kiện sai (i % j==0) sảy ra.
    list_nguyen_to = [i for i in lst if all(i % j != 0 for j in range(2, int(i**0.5) + 1))]
    print("Dãy số nguyên tố là:\n", " ".join(map(str, list_nguyen_to)))
    # Tạo list comprehension chứa các phần tử chia hết cho 7.
    list_nguyen_to_chia_het_bay = [i for i in list_nguyen_to if i % 7 == 0]
    return f"Dãy số nguyên tố chia hết cho 7 là:\n{" ".join(map(str,list_nguyen_to_chia_het_bay))}"


def tongsole(lst):
    total = 0
    for i in lst:
        total += i
    return f"Tổng các số lẻ trong dãy là: {total}"


def kiemtrasochinhphuong(lst):
    def scp(n):
        can = n**0.5
        if can == int(can):
            return True
        return False

    list_so_chinh_phuong = [number for number in lst if scp(number)]
    if len(list_so_chinh_phuong) == 0:
        return "Dãy không có số chính phương"
    return f"Dãy số chính phương là:\n{ " ".join(map(str, set(list_so_chinh_phuong)))}"
