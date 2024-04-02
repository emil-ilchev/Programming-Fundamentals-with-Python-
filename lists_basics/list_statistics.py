n = int(input())
positives_num = []
negatives_num = []
for i in range(n):
    num = int(input())
    if num >= 0:
        positives_num.append(num)
    else:
        negatives_num.append(num)
print(positives_num)
print(negatives_num)
print(f"Count of positives: {len(positives_num)}")
print(f"Sum of negatives: {sum(negatives_num)}")