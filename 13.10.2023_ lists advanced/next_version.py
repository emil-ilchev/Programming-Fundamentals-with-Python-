list_of_num = input().split(".")
version = [int(x) for x in list_of_num]
for el in range(len(version) - 1, -1, -1):
    if version[el] < 9:
        version[el] += 1
        break
    else:
        version[el] = 0
result = ".".join(map(str, version))
print(result)




# list_of_num = input().split(".")
# version = [int(x) for x in list_of_num]
# if version[2] == 9:
#     if version[1] == 9:
#         version[0] += 1
#         version[1] = 0
#         version[2] = 0
#     else:
#         version[1] += 1
#         version[2] = 0
# else:
#     version[2] += 1
#
# new_version = ".".join(map(str, version))
# print(new_version)
