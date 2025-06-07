def duplicate(all_list):
    seen = []
    removed_duplicate = []
    for i in all_list.split(", "):
        if i not in seen:
            removed_duplicate.append(i)
            seen.append(i)
    return ", ".join(removed_duplicate)


input_list = input()
result = duplicate(input_list)
print(result)
