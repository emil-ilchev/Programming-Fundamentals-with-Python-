def loading_bar(number):

    completed = f"[{'%' * number}{'.' * (10 - number)}]"
    if number == 10:
        print("100% Complete!")
        print(completed)
    else:
        print(completed)
        print("Still loading...")


num = int(input()) // 10
loading_bar(num)