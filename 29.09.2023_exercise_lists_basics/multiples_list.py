factor = int(input())
count = int(input())
result = []
for num in range(1, count + 1):
    result.append(num * factor)
print(result)


# factor = int(input())
# count = int(input())
# result = []
# current_number = factor
# for num in range(1, count + 1):
#     result.append(current_number)
#     current_number += factor
# print(result)


# factor = int(input())
# count = int(input())
# result = []
# for i in range(factor, factor * count + 1, factor):
#     result.append(i)
# print(result)

# factor = int(input())
# count = int(input())
# result = [x for x in range(factor, factor * count + 1, factor)]
# print(result)


# factor = int(input())
# count = int(input())
# print(list(range(factor, factor * count + 1, factor)))
