def factorial(first_number, second_number):
    factorial_first = first_number
    for num in range(first_number - 1, 0, -1):
        factorial_first *= num

    factorial_second = second_number
    for i in range(second_number - 1, 0, -1):
        factorial_second *= i
    result = factorial_first / factorial_second

    print(f"{result:.2f}")


first = int(input())
second = int(input())

factorial(first, second)
