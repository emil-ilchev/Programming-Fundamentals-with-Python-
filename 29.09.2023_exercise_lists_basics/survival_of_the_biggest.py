list_of_integer = input().split()
num_to_remove = int(input())
removed_list = []
for el in list_of_integer:
    current_int = int(el)
    removed_list.append(current_int)
for i in range(num_to_remove):
    smallest = min(removed_list)
    removed_list.remove(smallest)
print(", ".join(map(str, removed_list)))




