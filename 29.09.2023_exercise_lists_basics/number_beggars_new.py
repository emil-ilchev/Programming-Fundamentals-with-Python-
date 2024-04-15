string_of_integer = input().split(", ")
count_of_beggars = int(input())
sums = [0] * count_of_beggars
numbers = []
for num in string_of_integer:
    numbers.append(int(num))
for idx in range(len(numbers)):
    beggar_idx = idx % count_of_beggars
    sums[beggar_idx] += numbers[idx]
    # print(idx, beggar_idx, numbers[idx])
print(sums)
