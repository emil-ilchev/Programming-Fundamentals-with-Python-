
string_with_numbers = input().split(", ")
new_list = [index for index, el in enumerate(string_with_numbers) if int(el) % 2 == 0]
print(new_list)



# string_with_numbers = input().split(", ")
# new_list = []
# for index, el in enumerate(string_with_numbers):
#     if int(el) % 2 == 0:
#         new_list.append(index)
# print(new_list)