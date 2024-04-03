def countdown(seconds):
    if seconds == 0:
        print("Time's up!")
    elif seconds <= 120:
        print("seconds left", seconds)
        countdown(seconds - 1)


# print("Bắt đầu đếm lùi!!")
# countdown(20)
def permute(s, answer):
    if len(s) == 0:
        print(answer, end=" ")
        return
    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1 :]
        rest = left_substr + right_substr
        permute(rest, answer + ch)


# Gọi hàm
# permute("ABC", "")
