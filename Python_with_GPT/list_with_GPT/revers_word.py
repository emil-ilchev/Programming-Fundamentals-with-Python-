def reverse(word):
    if not word.isalpha():  # Проверява дали входът съдържа само букви
        raise ValueError("Това не е дума!")  # Хвърля грешка, ако не е дума
    return word[::-1]  # Обръща думата


try:
    input_word = input("Въведете дума: ")
    result = reverse(input_word)
    print(f"Обърнатата дума е: {result}")
except ValueError as e:
    print(e)

