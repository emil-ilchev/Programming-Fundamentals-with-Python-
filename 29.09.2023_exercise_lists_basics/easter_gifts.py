gifts = input().split()

while True:
    line = input().split()
    if line[0] == "No":
        break
    command_arg = line
    command = command_arg[0]

    if command == "OutOfStock":
        gift_name = command_arg[1]
        for i in range(len(gifts)):
            if gifts[i] == gift_name:
                gifts[i] = "None"
    if command == "Required":
        gift_name = command_arg[1]
        given_index = int(command_arg[2])
        if 0 <= given_index < len(gifts):
            gifts[given_index] = gift_name
    if command == "JustInCase":
        gift_name = command_arg[1]
        gifts[-1] = gift_name
print(' '.join([gift for gift in gifts if gift != 'None']))
