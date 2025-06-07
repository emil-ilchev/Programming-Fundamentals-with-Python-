def list_in_integer(my_list):
    even = [int(x) for x in my_list if x % 2 == 0]
    odd = [int(y) for y in my_list if y % 2 != 0]
    reversed_even = sorted(even, reverse=True)
    odd.sort()
    odd.extend(reversed_even)
    return odd


input_list = [3, 1, 2, 5, 4, 7, 6]
result = list_in_integer(input_list)
print(result)
