while True:
    while True:
        dict_nhan_vien = {
            "9876": ["nguyen van a", 1989, 10000000],
            "9874": ["nguyen van b", 1999, 20000000],
            "9871": ["nguyen van c", 1995, 9000000],
        }
        print("{:_^70}".format("MENU"))
        print("1.Tạo mới từ điển.")
        print("2.Thêm nhân viên với các thông tin được nhập từ bàn phím")
        print("3.Tìm kiếm nhân viên với giá trị mã nhân viên được nhập từ bàn phím.")
        print("4.Tăng lương 1 triệu cho nhân viên có mã là y, y được nhập từ bàn phím.")
        print("5.Xóa nhân viên có mã là z, z được nhập từ bàn phím.")
        print("6.Sắp xếp từ điển giảm dần theo năm sinh.")
        print("{:_^70}".format("END"))
        number = int(input("Nhập chức năng (1 - 6): "))
        if number == 1:
            print("Bạn đã chọn chức năng tạo mới từ điển.")
            dict_nhan_vien.clear()
            quantity = int(input("Nhập số lượng nhân viên: "))
            start = 1
            while start <= quantity:
                check_mnv, check_name, check_year = False, False, False
                error_mnv, error_name, error_year = True, True, True
                while True:
                    print(f"Mời nhập thông tin nhân viên thứ {start} là: ")
                    mnv = input("Nhập mã nhân viên (4 kí tự là sô): ")
                    if len(mnv) == 4 and mnv.isdigit():
                        check_mnv = True
                        error_mnv = False
                    name = input("Nhập tên NV(gồm 20 kí tự): ")
                    if name.isalpha() and len(name) == 20:
                        check_name = True
                        error_name = False
                    year = int(input("Nhập năm sinh: "))
                    if len(str(year)) == 4 and (1924 <= year <= 2024):
                        check_year = True
                        error_year = False
                    wage = int(input("Nhập lương: "))
                    if (
                        (check_mnv == True)
                        and (check_name == True)
                        and (check_year == True)
                    ):
                        dict_nhan_vien[mnv] = [name, year, wage]
                        start += 1
                        break
                    else:
                        if error_mnv:
                            print("Mời nhập lại do sai định dạng mnv:")
                        elif error_name:
                            print("Mời nhập lại do sai định dạng tên.")
                        else:
                            print("Mời nhập lại do sai địng dạng năm sinh.")
            print(f"Danh sách sau khi được tạo mới là:\n{dict_nhan_vien}")
        elif number == 2:
            print("Bạn đã chọn chức năng thêm nhân viên.")
            quantity = int(input("Nhập số lượng nhân viên: "))
            start = 1
            while start <= quantity:
                check_mnv, check_name, check_year = False, False, False
                error_mnv, error_name, error_year = True, True, True
                check_in = False
                while True:
                    print(f"Mời nhập thông tin nhân viên thứ {start} là: ")
                    mnv = input("Nhập mã nhân viên (4 kí tự là sô): ")
                    if len(mnv) == 4 and mnv.isdigit() and (mnv not in dict_nhan_vien):
                        check_mnv = True
                        error_mnv = False
                        check_in = True
                    name = input("Nhập tên NV(gồm 20 kí tự): ")
                    if name.isalpha() and len(name) == 20:
                        check_name = True
                        error_name = False
                    year = int(input("Nhập năm sinh: "))
                    if len(str(year)) == 4 and (1924 <= year <= 2024):
                        check_year = True
                        error_year = False
                    wage = int(input("Nhập lương: "))
                    if (
                        (check_mnv == True)
                        and (check_name == True)
                        and (check_year == True)
                        and (check_in == True)
                    ):
                        dict_nhan_vien[mnv] = [name, year, wage]
                        start += 1
                        break
                    else:
                        if error_mnv:
                            print("Mời nhập lại do sai định dạng mnv:")
                        elif error_name:
                            print("Mời nhập lại do sai định dạng tên.")
                        elif check_in:
                            print("Mời nhập lại do trùng mnv cũ.")
                        else:
                            print("Mời nhập lại do sai địng dạng năm sinh.")
            print(f"Danh sách sau khi được tạo mới là:\n{dict_nhan_vien}")
        elif number == 3:
            print("Bạn đã chọn chức năng tìm kiếm nhân viên.")
            while True:
                find_mnv = input("Nhập mã nhân viên cần tìm: ")
                if (
                    len(find_mnv) == 4
                    and find_mnv.isdigit()
                    and find_mnv in dict_nhan_vien
                ):
                    print(
                        f"Mã {find_mnv} có thông tin nhân là:\nHọ và tên: {dict_nhan_vien[find_mnv][0]}\nNăm sinh: {dict_nhan_vien[find_mnv][1]}\nLương: {dict_nhan_vien[find_mnv][2]}"
                    )
                    break
                else:
                    print(f"Mã {find_mnv} này không có trong danh sách nhân viên.")

        elif number == 4:
            print(
                "Bạn đã chọn chức năng tăng 1 triệu cho nhân viên có mã được nhập từ bàn phím."
            )
            check_menu = False
            while True:
                code_update_wage = input("Nhập mã nhân viên cần tìm: ")
                if (
                    len(code_update_wage) == 4
                    and code_update_wage.isdigit()
                    and code_update_wage in dict_nhan_vien
                ):
                    dict_nhan_vien[code_update_wage][2] = (
                        dict_nhan_vien[code_update_wage][2]
                    ) + 1000000
                    print(f"Danh sách sau khi tăng lương là:\n{dict_nhan_vien}")
                    check_menu = True
                    break
                else:
                    print(
                        f"Mã {code_update_wage} này không có trong danh sách nhân viên."
                    )
            if check_menu:
                break
        elif number == 5:
            print("Bạn đã chọn chức năng xóa nhân viên theo mã.")
            while True:
                clear_mnv = input("Nhập mã nhân viên cần tìm: ")
                if (
                    len(clear_mnv) == 4
                    and clear_mnv.isdigit()
                    and clear_mnv in dict_nhan_vien
                ):
                    del dict_nhan_vien[clear_mnv]
                    print(f"Danh sách sau khi xóa mã {clear_mnv} là:\n{dict_nhan_vien}")
                    break
                else:
                    print(f"Mã {clear_mnv} này không có trong danh sách nhân viên.")
        elif number == 6:
            sort_year = dict(
                sorted(dict_nhan_vien.items(), key=lambda x: x[1][1], reverse=True)
            )
            print(f"Danh sách sau khi sắp xếp giảm dần theo năm sinh là:\n{sort_year}")
            break
        else:
            print("Chức năng bạn vừa nhập không có trong menu.")
            print("Mời nhập lại.")
    check = input("Bạn có muốn chọn chức năng tiếp không(y/n): ").lower()
    if check == "n":
        break
