def min_and_max_values():
    numbers = input().split()
    min_number = min(int(x) for x in numbers)
    max_number = max(int(x) for x in numbers)
    sum_number = sum(int(x) for x in numbers)
    return print(f"The minimum number is {min_number}\n"
                 f"The maximum number is {max_number}\n"
                 f"The sum number is: {sum_number}")


min_and_max_values()
