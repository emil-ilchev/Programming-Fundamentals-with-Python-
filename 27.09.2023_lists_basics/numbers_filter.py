n = int(input())
full_list = []
even = []
odd = []
negative_list = []
positive_list = []
command = ""
for i in range(n):
    numbers = int(input())
    full_list.append(numbers)
command = input()

for num in full_list:
    if num >= 0:
        positive_list.append(num)
    if num < 0:
        negative_list.append(num)
    if num % 2 == 0:
        even.append(num)
    if num % 2 != 0:
        odd.append(num)
if command == "positive":
    print(positive_list)
elif command == "negative":
    print(negative_list)
elif command == "odd":
    print(odd)
elif command == "even":
    print(even)



# n = int(input())
# list_of_numbers = []
# final_list = []
#
# for i in range(n):
#     numbers = int(input())
#     list_of_numbers.append(numbers)
#
# command = input()
#
# for num in list_of_numbers:
#     if command == "even":
#         if num % 2 == 0:
#             final_list.append(num)
#     elif command == "odd":
#         if num % 2 != 0:
#             final_list.append(num)
#     elif command == "negative":
#         if num < 0:
#             final_list.append(num)
#     elif command == "positive":
#         if num >= 0:
#             final_list.append(num)
#
# print(final_list)





