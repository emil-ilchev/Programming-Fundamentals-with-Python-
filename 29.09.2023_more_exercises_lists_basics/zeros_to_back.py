string_as_integer = input().split(", ")
numbers = [int(num) for num in string_as_integer]
new_numbers = []
count = numbers.count(0)
while 0 in numbers:
    numbers.remove(0)
numbers.extend([0] * count)
print(numbers)



string_as_integer = input().split(", ")
numbers = [int(num) for num in string_as_integer]
count_of_zero = 0
non_zero_numbers = []
for num in numbers:
    if num != 0:
        non_zero_numbers.append(num)
    else:
        count_of_zero += 1
non_zero_numbers.extend([0] * count_of_zero)
print(non_zero_numbers)



string_of_integers = input().split(', ')
list_of_integer = []

for i in range(len(string_of_integers)):
    string_of_integers.remove("0")
    string_of_integers.append("0")
list_of_integer = [int(x) for x in string_of_integers]

print(list_of_integer)
