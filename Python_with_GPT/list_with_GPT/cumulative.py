def cumulative_difference(numbers):
    numbers = [int(x) for x in numbers.split(", ")]
    result = []
    cumulative_sum = 0
    for num in numbers:
        result.append(num - cumulative_sum)
        cumulative_sum += num
    return result


input_list = input()
output = cumulative_difference(input_list)
print(output)
