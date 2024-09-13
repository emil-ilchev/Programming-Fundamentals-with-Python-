num_of_wagons = int(input())
command = input()
train = [0 for x in range(num_of_wagons)]
while command != "End":
    parts = command.split()
    action = parts[0]
    if action == "add":
        train[-1] += int(parts[1])
    elif action == "insert":
        index = int(parts[1])
        people = parts[2]
        train[index] += int(people)
    elif action == "leave":
        index = int(parts[1])
        people = parts[2]
        train[index] -= int(people)
    command = input()

print(train)
