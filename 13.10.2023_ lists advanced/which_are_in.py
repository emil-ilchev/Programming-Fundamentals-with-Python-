first_sequences = input().split(", ")
second_sequences = input().split(", ")

substring = []

for first_string in first_sequences:
    for second_strings in second_sequences:
        if first_string in second_strings:
            substring.append(first_string)
            break
print(substring)


# first_string = input().split(", ")
# second_string = input().split(", ")
#
# new_list = [first_el for first_el in first_string if any(first_el in second_el for second_el in second_string)]
# print(new_list)