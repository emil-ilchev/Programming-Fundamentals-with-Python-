def rounding(numbers):
    result = [float(x) for x in numbers]
    rounded = [round(el) for el in result]
    return rounded


num = input().split()
print(rounding(num))


def rounding(numbers):
    result = [round(float(x)) for x in numbers]
    return result


num = input().split()
print(rounding(num))