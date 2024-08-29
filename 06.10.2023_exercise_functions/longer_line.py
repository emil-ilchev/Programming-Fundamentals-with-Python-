import math


def longer_lines(x1, y1, x2, y2, x3, y3, x4, y4):

    first_line = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    second_line = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)

    if first_line > second_line:
        return x1, y1, x2, y2
    else:
        return x3, y3, x4, y4


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

result = longer_lines(x1, y1, x2, y2, x3, y3, x4, y4)
print(result)
