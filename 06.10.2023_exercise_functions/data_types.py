def data_type():

    command = input()
    sign = input()
    if command == "int":
        return int(sign) * 2
    elif command == "real":
        return f"{float(sign) * 1.5:.2f}"
    elif command == "string":
        return f"${sign}$"


result = data_type()
print(result)


# def process_input(data_type):
#     if data_type == "int":
#         number = int(input())
#         print(number * 2)
#     elif data_type == "real":
#         number = float(input())
#         print(f"{number * 1.5:.2f}")
#     elif data_type == "string":
#         text = input()
#         print(f"${text}$")
#     else:
#         print("Invalid data type")
#
#
# user_data = input()
# process_input(user_data)
