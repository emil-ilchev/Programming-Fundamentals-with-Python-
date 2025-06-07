def average_above_5(list_of_num):
    over_5 = [int(x) for x in list_of_num if int(x) >= 5]
    if len(over_5) < 1:
        return "Няма числа над 5"
    else:
        average = sum(over_5) / len(over_5)
        return f"{average:.2f}"


user_input = input().split(", ")
result = average_above_5(user_input)
print(result)
