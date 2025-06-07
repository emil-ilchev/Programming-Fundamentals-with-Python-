def remove_duplicates(numbers):
    unique_numbers = []
    seen = set()
    for el in numbers.split(", "):
        if el not in seen:
            unique_numbers.append(el)
            seen.add(el)
    return ", ".join(unique_numbers)


list_number = input()
result = remove_duplicates(list_number)
print(result)
