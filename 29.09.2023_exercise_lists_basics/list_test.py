# numbers = [1, 2, 2, 3, 2, 5, 4, 2, 6, 8, 2, 3]
# while 2 in numbers:
#     numbers.remove(2)
# print(numbers)

# my_list = [1, 2, 3, "a", " b", "c", "d", " e", "f"]
# char = my_list.pop(-3)
# print(char)
# print(my_list)

# my_list = ["a", " b", "c", "d", " e", "f"]
# print(' '.join([x for x in my_list if x != "d"]))

# my_list = [1, 2, 3, "a", " b", "c", "d", " e", "f"]
# while len(my_list) < 20:
#     my_list.append("a")
# print(my_list)

# my_list = [1, 2, 3, "a", " b", "c", "d", " e", "f"]
# my_list.insert(5, "Pesho")
# print(my_list)

# my_list = [1, 2, 3, "b", "a", " b", "c", "a", "a", "a", "d", " e", "a", "f"]
# char = my_list.index("a")
# print(char)

# my_list = [1, 2, 3, "b", "a", " b", "c", "a", "a", "a", "d", " e", "a", "f"]
# repetition = my_list.count("a")
# print(repetition)
# while my_list.count("a") > 1:
#     my_list.remove("a")
# print(my_list)

# my_list = [1, 2, 3, "b", "a", " b", "c", "a", "a", "a", "d", " e", "a", "f"]
# indexes = []
# for index, element in enumerate(my_list):
#     if element == "a":
#         indexes.append(index)
# print(indexes)

# my_list = [1, 2, 3, "b", "a", " b", "c", "a", "a", "a", "d", " e", "a", "f"]
# my_list.reverse()
# print(my_list)
# print(my_list[::-1])

# my_list = [1, 2, 3, "b", "a", " b", "c", "a", "a", "a", "d", " e", "a", "f"]
# del my_list[3]
# print(my_list)

# my_list = [1, 2, 3, "b", "a", " b", "c", "a", "a", "a", "d", " e", "a", "f"]
# my_list.remove("a")
# print(my_list)

# my_list = [1, 2, 3, 4, 5]
# my_second_list = my_list
# my_second_list.remove(2)
# print(my_list)
# print(my_second_list)
# #
# my_list = [1, 2, 3, 4, 5]
# my_second_list = my_list.copy()
# my_second_list.remove(2)
# print(my_list)
# print(my_second_list)

# my_list = ["1", "2", "3", "4", "5"]
# my_list.remove("1")
# print(my_list)

# text = list(input())
# stack = []
# for i in range(len(text)):
#     stack.append(text.pop())
# print("".join(stack))

# text = list(input())
# while text:
#     removed_elements = text.pop()
#     print(removed_elements, end="")

# text = input()
# print(text[::-1])
