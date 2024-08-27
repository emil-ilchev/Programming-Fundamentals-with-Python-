def tribonacci_numbers(numbers):

    tribonacci_list = [1, 1, 2]

    while len(tribonacci_list) < numbers:
        next_number = tribonacci_list[-1] + tribonacci_list[-2] + tribonacci_list[-3]
        tribonacci_list.append(next_number)

    print(" ".join(map(str, tribonacci_list[:numbers])))


user_input = int(input())
tribonacci_numbers(user_input)
