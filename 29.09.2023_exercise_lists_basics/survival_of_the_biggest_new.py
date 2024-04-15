list_of_integer = input().split()
n = int(input())

numbers = [int(x) for x in list_of_integer]
for num in range(n):
    min_number = min(numbers)
    numbers.remove(min_number)
print(", ".join(map(str, numbers)))
