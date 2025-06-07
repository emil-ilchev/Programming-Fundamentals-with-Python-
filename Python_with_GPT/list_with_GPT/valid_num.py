def my_list(list1, user_index):
    try:
        return list1[user_index]
    except IndexError:
        return "Индексът е извън границите на списъка."


first_list = [10, 20, 30, 40, 50]

while True:
    try:
        user_input = int(input("въведете индекс"))
        result = my_list(first_list, user_input)
        if result == "Индексът е извън границите на списъка.":
            print(result)
        else:
            print(f"Елементът на индекс {user_input} е: {result}")
            break
    except ValueError:
        print("Моля, въведете валиден индекс (цяло число).")
