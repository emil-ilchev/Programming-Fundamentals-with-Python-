import math

def center_point(x1, y1, x2, y2):

    first_point = math.sqrt((x1 ** 2) + (y1 ** 2))
    second_point = math.sqrt((x2 ** 2) + (y2 ** 2))
    if first_point > second_point:
        return math.floor(x2), math.floor(y2)
    else:
        return math.floor(x1), math.floor(y1)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

result = center_point(x1, y1, x2, y2)
print(result)
