numbers_at_str = input().split(", ")

numbers = [int(x) for x in numbers_at_str]
positive = [x for x in numbers if x >= 0]
negative = [x for x in numbers if x < 0]
even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]

print(f"Positive: {', '.join(map(str, positive))}")
print(f"Negative: {', '.join(map(str, negative))}")
print(f"Even: {', '.join(map(str, even))}")
print(f"Odd: {', '.join(map(str, odd))}")



# def positives(num):
#     return ', '.join([x for x in num if int(x) >= 0])
#
# def negatives(num):
#     return ', '.join([x for x in num if int(x) < 0])
#
# def even(num):
#     return ', '.join([x for x in num if int(x) % 2 == 0])
#
# def odd(num):
#     return ', '.join([x for x in num if int(x) % 2 != 0])
#
#
# numbers_at_str = input().split(", ")
#
# print(f"Positives: {positives(numbers_at_str)}")
# print(f"Negative: {negatives(numbers_at_str)}")
# print(f"Even: {even(numbers_at_str)}")
# print(f"Odd: {odd(numbers_at_str)}")
