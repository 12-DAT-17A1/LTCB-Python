dict_number = dict()
for number in range(1, 101):
    chain_binary = ""
    nguyen = number
    while nguyen != 0:
        du = nguyen % 2
        nguyen //= 2
        chain_binary = str(du) + chain_binary
    dict_number["value" + str(number)] = (number, chain_binary)
print(dict_number)
