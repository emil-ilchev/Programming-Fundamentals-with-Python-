first_num = int(input())
second_num = int(input())
third_num = int(input())


def sum_numbers(a, b):
    return a + b


def subtract(a, b, c):
    return sum_numbers(a, b) - c


result = subtract(first_num, second_num, third_num)
print(result)
