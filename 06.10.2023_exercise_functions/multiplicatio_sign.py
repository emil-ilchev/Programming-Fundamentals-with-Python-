def multiplication():
    negative_count = 0

    for i in range(3):
        number = int(input())

        if number == 0:
            print("Zero")
        if number < 0:
            negative_count += 1
    if negative_count % 2 == 0:
        return "positive"
    else:
        return "negative"


result = multiplication()
print(result)
