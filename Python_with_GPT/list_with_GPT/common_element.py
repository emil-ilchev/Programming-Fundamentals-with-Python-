def common_elements(first, second):
    new_list = []
    for el in first.split(", "):
        for i in second.split(", "):
            if i == el and i not in new_list:
                new_list.append(i)
    final = ", ".join(new_list)
    return final


first_list = input()
second_list = input()
result = common_elements(first_list, second_list)
print(result)
