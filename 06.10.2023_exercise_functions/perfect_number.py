def perfect_number(number):

    perfect_num = 0
    for num in range(1, number):
        if number % num == 0:
            perfect_num += num
    if perfect_num == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


user_input = int(input())
perfect_number(user_input)




# def is_perfect_number(number):
#     divisor_sum = sum(divisor for divisor in range(1, number) if number % divisor == 0)
#
#     if divisor_sum == number:
#         return "We have a perfect number!"
#     else:
#         return "It's not so perfect."
#
#
# number = int(input())
#
# result = is_perfect_number(number)
# print(result)
