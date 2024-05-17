def clearchain(chain):
    chain_new = ""
    for chr in chain:
        if chr.upper() in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"}:
            chain_new += chr.upper()
    return chain_new


def nhanbietso(chain):
    print(f"Chuỗi sau khi loại bỏ các kí tự thừa là: {chain}")
    chain = chain.upper()
    for str_number in chain:
        if str_number == "0" or str_number == "1":
            continue
        else:
            break
    else:
        print("Hệ cơ số 2")
        chain_number_new = chain[::-1]
        total = 0
        count_tt = 0
        for str_number in chain_number_new:
            if str_number == "1":
                total += 2**count_tt
            count_tt += 1
        return f"{chain} hệ cơ số 2 sang hệ cơ số 10 là: {total}"
    for str_number in chain:
        if str_number >= "0" and str_number <= "7":
            continue
        else:
            break
    else:
        print("Hệ cơ số 8")
        total = 0
        count_tt = 0
        for str_number in chain[::-1]:
            total += int(str_number) * (8**count_tt)
            count_tt += 1
        return f"{chain} hệ cơ số 8 sang hệ cơ số 10 là: {total}"
    for str_number in chain:
        if (str_number >= "0" and str_number <= "9") or ("A" <= str_number <= "F"):
            continue
        else:
            break
    else:
        print("Hệ cơ số 16")
        dict_number = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
        total = 0
        count_tt = 0
        for str_number in chain.upper()[::-1]:
            if "0" <= str_number <= "9":
                total += int(str_number) * (16**count_tt)
                count_tt += 1
            else:
                total += dict_number[str_number] * (16**count_tt)
                count_tt += 1
        return f"{chain} hệ cơ số 16 sang hệ cơ số 10 là: {total}"
    return "Không thuộc hệ cơ số nào"


def chuyendoihe2():
    chain_number = input("Nhập chuỗi số hệ cơ số 2: ")
    chain_number_new = chain_number[::-1]
    total = 0
    count_tt = 0
    for str_number in chain_number_new:
        if str_number == "1":
            total += 2**count_tt
        count_tt += 1
    return f"{chain_number} hệ cơ số 2 sang hệ cơ số 10 là: {total}"


def chuyendoihe8():
    chain = input("Nhập chuỗi số hệ 8: ")
    total = 0
    count_tt = 0
    for str_number in chain[::-1]:
        total += int(str_number) * (8**count_tt)
        count_tt += 1
    return f"{chain} hệ cơ số 8 sang hệ cơ số 10 là: {total}"


def chuyendoihe16():
    dict_number = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    chain = input("Nhập chuỗi số hệ 16: ")
    total = 0
    count_tt = 0
    for str_number in chain.upper()[::-1]:
        if "0" <= str_number <= "9":
            total += int(str_number) * (16**count_tt)
            count_tt += 1
        else:
            total += dict_number[str_number] * (16**count_tt)
            count_tt += 1
    return f"{chain} hệ cơ số 16 sang hệ cơ số 10 là: {total}"
