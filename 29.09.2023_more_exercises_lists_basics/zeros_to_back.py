string_as_integer = input().split(", ")
numbers = [int(num) for num in string_as_integer]
new_numbers = []
count = numbers.count(0)
while 0 in numbers:
    numbers.remove(0)
numbers.extend([0] * count)
print(numbers)

