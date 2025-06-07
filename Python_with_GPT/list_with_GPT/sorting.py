# def sorting(list_number):
#     try:
#         list_number = [int(x.strip()) for x in list_number.split(", ")]
#         list_number.sort()
#         return ", ".join(map(str, list_number))
#     except ValueError:
#         return "not ok"
#
#
# input_list = input()
# result = sorting(input_list)
# print(result)


def min_max(number):
    try:
        number = number.replace(",", ", ").replace("  ", " ")
        number = [int(x) for x in number.split(", ")]
        min_num = min(number)
        max_num = max(number)
        return f"max: {max_num}, min: {min_num}"
    except ValueError:
        return "Моля, въведете валиден списък от числа"


input_num = input()
result = min_max(input_num)
print(result)
