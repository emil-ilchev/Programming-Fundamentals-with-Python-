import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def closer_point_to_center(x1, y1, x2, y2):
    distance1 = math.sqrt(x1 ** 2 + y1 ** 2)
    distance2 = math.sqrt(x2 ** 2 + y2 ** 2)

    if distance1 <= distance2:
        return math.floor(x1), math.floor(y1), math.floor(x2), math.floor(y2)
    else:
        return math.floor(x2), math.floor(y2), math.floor(x1), math.floor(y1)

def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    line1_length = calculate_distance(x1, y1, x2, y2)
    line2_length = calculate_distance(x3, y3, x4, y4)

    if line1_length >= line2_length:
        x1, y1, x2, y2 = closer_point_to_center(x1, y1, x2, y2)
        return f"({x1}, {y1})({x2}, {y2})"
    else:
        x3, y3, x4, y4 = closer_point_to_center(x3, y3, x4, y4)
        return f"({x3}, {y3})({x4}, {y4})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

result = longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
print(result)
