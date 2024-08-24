def sum_of_num():
    number = input()
    sum_of_odd_digits = [int(x) for x in number if int(x) % 2 != 0]
    sum_of_even_digits = [int(x) for x in number if int(x) % 2 == 0]
    return f"Odd sum = {sum(sum_of_odd_digits)}, Even sum = {sum(sum_of_even_digits)}"


result = sum_of_num()
print(result)
