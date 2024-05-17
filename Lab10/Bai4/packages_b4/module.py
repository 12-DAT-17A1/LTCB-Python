def giaiptbacnhat1an(a, b):
    if a == 0:
        if b == 0:
            return "vo so nghiem"
        else:
            return "vo nghiem"
    return -b / a


def giaiptbachai(a, b, c):
    if a != 0:
        delta = b**2 - 4 * a * c
        if delta > 0:
            print("Phương trình có hai nghiệm phân biệt là:")
            x = (-b + (delta) ** 0.5) / (2 * a)
            y = (-b - (delta) ** 0.5) / (2 * a)
            return f"x = {x}\ny = {y}"
        elif delta == 0:
            print("Phương trình có một nghiệm kép.")
            return f"x = {-b/2*a}"
        else:
            print("Phương trình vô nghiệm.")
