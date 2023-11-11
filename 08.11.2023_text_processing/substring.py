
first_string = input().strip()
second_string = input().strip()

while first_string in second_string:
    second_string = second_string.replace(first_string, '', 1)

print(second_string)
