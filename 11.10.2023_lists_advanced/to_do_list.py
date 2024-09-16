notes = [0] * 10
command = input()
while True:
    if command == "End":
        final_list = [x for x in notes if x != 0]
        break
    importance, note = command.split("-")
    importance = int(importance)
    notes.insert(importance, note)

    command = input()
print(final_list)
