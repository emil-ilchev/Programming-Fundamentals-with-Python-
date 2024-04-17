people = input().split()
k = int(input())
people = [int(x) for x in people]
index = 0
executed = []

for _ in range(len(people)):
    index = (index + k - 1) % len(people)
    executed.append(people.pop(index))

print("[" + ",".join(map(str, executed)) + "]")



# people = list(map(int, input().split()))
# k = int(input())
# executed = []
# index = 0
#
# while len(people) > 0:
#     index = (index + k - 1) % len(people)
#     executed.append(people.pop(index))
# print("[" + ",".join(map(str, executed)) + "]")



