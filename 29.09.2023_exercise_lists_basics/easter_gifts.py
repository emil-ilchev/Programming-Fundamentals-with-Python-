gifts = input().split()

while True:
    line = input()
    if line == "No Money":
        break
    command_arg = line.split()
    command = command_arg[0]
    if command == "OutOfStock":
        pass
