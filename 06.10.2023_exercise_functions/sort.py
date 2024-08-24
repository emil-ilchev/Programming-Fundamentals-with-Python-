def sort_numbers():
    numbers = input().split()
    sorted_list = [int(x) for x in numbers]
    return sorted(sorted_list)


result = sort_numbers()
print(result)


def sort_numbers():
    numbers = input().split()
    sorted_list = sorted(int(x) for x in numbers)
    return sorted_list


result = sort_numbers()
print(result)
