
b = [21, 0, 13, 41, 56, 78, 91, 10, 101]


def max_arry(b):
    max_num = b[0]
    min_num = b[0]
    for i in range(len(b)):
        if b[i] > max_num:
            max_num = b[i]
        if b[i] < min_num:
            min_num = b[i]

    return f"Min Number: {min_num}, Max Number: {max_num}"


print(max_arry(b))
