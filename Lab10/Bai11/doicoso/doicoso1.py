def enter_number(n):
    return n


def henhiphan(n):
    chain = ""
    nguyen = n
    while nguyen != 0:
        du = nguyen % 2
        chain = str(du) + chain
        nguyen //= 2
    return chain


def hebatphan(n):
    chain = ""
    nguyen = n
    while nguyen != 0:
        du = nguyen % 8
        chain = str(du) + chain
        nguyen //= 8
    return chain


def hethaplucphan(n):
    return hex(n)[2:].upper()
