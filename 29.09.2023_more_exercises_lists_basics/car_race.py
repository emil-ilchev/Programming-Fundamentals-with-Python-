sequence_of_numbers = input().split()
numbers = [int(num) for num in sequence_of_numbers]
distance = len(numbers) // 2
left_car_time = 0
left_car_counter = 0
for num in range(distance):
    if numbers[num] != 0:
        left_car_time += numbers[num]
        left_car_counter += 1
    if numbers[num] == 0:
        left_car_time *= 0.8
        left_car_counter += 1

right_car_time = 0
right_car_counter = 0
for num in range(distance):
    negative_idx = -num - 1
    if numbers[negative_idx] != 0:
        right_car_time += numbers[negative_idx]
        right_car_counter += 1
    if numbers[negative_idx] == 0:
        right_car_time *= 0.8
        right_car_counter += 1
    if right_car_counter == distance:
        break

if right_car_time < left_car_time:
    print(f"The winner is right with total time: {right_car_time:.1f}")
else:
    print(f"The winner is left with total time: {left_car_time:.1f}")
