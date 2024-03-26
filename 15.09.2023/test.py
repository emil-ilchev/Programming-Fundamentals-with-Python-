# name = "abcdefghijklmnopqrstuvwxyz"
# print(name[::-1])
# print((name[::]), end=" ")
# print(123456, end=" ")
# print("Hello")
#
# # for number in range(1, 11):
# #     print(str(number), end=" ")
# # print(f"{1234.5678:.2f}")
#
# from math import ceil
#
# students = int(input())
# lectures = int(input())
# bonus = int(input())
# max_attendances = 0
#
# for i in range(students):
#     attendances = int(input())
#     max_attendances = max(max_attendances, attendances)
# total_bonus = 0
# if lectures != 0:
#     total_bonus = max_attendances / lectures * (5 + bonus)
#
# print(f"Max Bonus: {ceil(total_bonus)}.")
# print(f"The student has attended {max_attendances} lectures.")
#
# ex_list = [1, 2]
# for index, elements in enumerate(ex_list):
#     print(index, elements)


# nums = {1: "one", 2: "two", 0: "zero"}
#
# for key in nums.keys():
#     print(key)
#
# for value in nums.values():
#     print(value)
#
# for key, value in nums.items():
#     print(key, value)

# num = 1
# user = int(input())
# if num < user:
#     while num < user:
#         print(num)
#         num += 1
# if num > user:
#     num = -1
#     while num > user:
#         print(num)
#         num -= 1


# counter = 0
# sum = 0
# limit = int(input())
# while sum < limit:
#     counter += 1
#     sum += counter
#     print(str(counter) + " +", end=" ")
# print("= " + str(sum))


