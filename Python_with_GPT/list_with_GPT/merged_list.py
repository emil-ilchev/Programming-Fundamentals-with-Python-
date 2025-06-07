def merge_list(list1, list2):
    merged_list = list1 + list2
    return merged_list


input_list1 = input("Въведете елементи на първия списък, разделени със запетая: ")
first_list = [x.strip() for x in input_list1.split(",")]

input_list2 = input("Въведете елементи на втория списък, разделени със запетая: ")
second_list = [x.strip() for x in input_list2.split(",")]

result = merge_list(first_list, second_list)
print(result)
