def palindrome_integers():
    list_of_integers = input().split(", ")

    for number in list_of_integers:
        if number == number[::-1]:
            print(True)
        else:
            print(False)


palindrome_integers()


# def palindrome_integers():
#     list_of_integers = input().split(", ")
#
#     for number in list_of_integers:
#         if len(number) % 2 != 0:
#             middle_of_list = len(number) // 2
#             left_side = number[:middle_of_list]
#             right_side = number[:middle_of_list:-1]
#             if left_side == right_side:
#                 print(True)
#             else:
#                 print(False)
#         else:
#             middle_of_list = len(number) // 2
#             left_side = number[:middle_of_list]
#             right_side = number[:middle_of_list - 1:-1]
#             if left_side == right_side:
#                 print(True)
#             else:
#                 print(False)
#
#
# palindrome_integers()
