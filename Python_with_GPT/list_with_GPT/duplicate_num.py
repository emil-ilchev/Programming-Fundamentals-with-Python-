def remove_duplicates(list_duplicates):
    try:
        list_duplicates = list_duplicates.replace(",", ", ").replace("  ", " ")
        seen = set()
        checked = []
        for i in list_duplicates.split(", "):
            if i not in seen:
                checked.append(i)
            seen.add(i)
        return ", ".join(checked)
    except ValueError:
        return "Моля, въведете валиден списък"


user_input = input()
result = remove_duplicates(user_input)
print(result)
