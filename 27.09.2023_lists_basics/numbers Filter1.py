n = int(input())
list_of_numbers = []
final_list = []

for i in range(n):
    numbers = int(input())
    list_of_numbers.append(numbers)

command = input()

for num in list_of_numbers:
    if command == "even":
        if num % 2 == 0:
            final_list.append(num)
    elif command == "odd":
        if num % 2 != 0:
            final_list.append(num)
    elif command == "negative":
        if num < 0:
            final_list.append(num)
    elif command == "positive":
        if num >= 0:
            final_list.append(num)

print(final_list)
