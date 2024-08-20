def calculations(input_operator, first_num, second_num):
    if input_operator == "multiply":
        return first_num * second_num
    elif input_operator == "divide":
        if second_num == 0:
            return "Error"
        return int(first_num / second_num)
    elif input_operator == "add":
        return first_num + second_num
    elif input_operator == "subtract":
        return first_num - second_num


operator = input()
first = int(input())
second = int(input())

result = calculations(operator, first, second)
print(result)
