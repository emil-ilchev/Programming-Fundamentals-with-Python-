def characters(a, b):
    start = ord(a)
    final = ord(b)
    element = []
    while start < final - 1:
        start += 1
        element.append(start)

    new_list = [chr(x) for x in element]

    return " ".join(new_list)


first = input()
second = input()
print(characters(first, second))


# def characters(a, b):
#     # Получаваме ASCII стойностите на символите
#     start = ord(a)
#     final = ord(b)
#
#     # Проверяваме дали първият символ е по-малък, за да определим посоката
#     if start < final:
#         result = [chr(x) for x in range(start + 1, final)]
#     else:
#         result = [chr(x) for x in range(final + 1, start)]
#
#     # Връщаме резултата като един string
#     return " ".join(result)
#
#
# first = input("Въведете първия символ: ")
# second = input("Въведете втория символ: ")
# print(characters(first, second))
