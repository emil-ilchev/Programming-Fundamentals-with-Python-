def check(check_list, amount):
    check_list = check_list.split(", ")
    return amount in check_list


user_input = input()
amount_input = input()
result = check(user_input, amount_input)
print(result)
