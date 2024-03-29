# Tạo hàm in ra dãy fibonacci không quá 10 số hạng.
def fibonacci(n):
    x = 0
    y = 1
    i = 0
    while i < n:
        print(x, end=" ")
        x, y = y, x + y
        i += 1


# fibonacci(10)
import msvcrt


def xemascii():
    while True:
        char = msvcrt.getch()
        if ord(char) == 27:
            break
        print("Giá trị ascii của ký tự '%s' là %d" % (char.decode(), ord(char)))


def func():
    print("func() trong module.py")


print("Đầu của module.py")

if __name__ == "__main__":
    print("module.py đang được chạy trực tiếp")
else:
    print("module.py đã được import vào một module khác")
