initial_list = input().split("!")
command = input()
while True:
    if command == "Go Shopping!":
        break
    parts = command.split()
    action = parts[0]
    item = parts[1] if len(parts) > 1 else None

    if action == "Urgent" and item not in initial_list:
        initial_list.insert(0, item)
    elif action == "Unnecessary" and item in initial_list:
        initial_list.remove(item)
    elif action == "Correct" and len(parts) > 2:
        old_item = parts[1]
        new_item = parts[2]
        if old_item in initial_list:
            index = initial_list.index(old_item)
            initial_list[index] = new_item
    elif action == "Rearrange" and item in initial_list:
        initial_list.remove(item)
        initial_list.append(item)

    command = input()
result = ", " .join(initial_list)
print(result)
