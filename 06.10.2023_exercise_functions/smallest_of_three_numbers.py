import sys


def smallest_numbers():
    min_num = sys.maxsize
    for i in range(3):
        number_input = int(input())
        if number_input < min_num:
            min_num = number_input
    return min_num


print(smallest_numbers())




def smallest_numbers():
    smallest = []
    for i in range(3):
        number_input = int(input())
        smallest.append(number_input)
    return min(smallest)


print(smallest_numbers())



# def find_smallest_of_three():
#     num1 = int(input("Въведете първото число: "))
#     num2 = int(input("Въведете второто число: "))
#     num3 = int(input("Въведете третото число: "))
#
#     return min(num1, num2, num3)
#
# result = find_smallest_of_three()
# print("Най-малкото число е:", result)
