def positive_negative(nums):
    nums = [int(x) for x in nums.split(", ")]
    positives = [x for x in nums if x > 0]
    negatives = [y for y in nums if y < 0]
    return positives, negatives


numbers = input()
positiv, negativ = positive_negative(numbers)
print("Положителни числа:", positiv)
print("Отрицателни числа:", negativ)
