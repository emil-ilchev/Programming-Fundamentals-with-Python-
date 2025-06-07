while True:
    try:
        first_num = float(input("Въведете число"))
        second_num = float(input("Въведете второ число"))
        result = first_num / second_num
        print(f"Резултатът е {result}")
        break
    except ZeroDivisionError:
        print("Грешка: Делението на нула не е възможно. Опитайте отново.")
    except ValueError:
        print("Грешка: Моля, въведете валидно число.")
