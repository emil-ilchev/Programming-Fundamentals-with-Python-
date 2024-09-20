words = input().split()
filtered = [x for x in words if len(x) % 2 == 0]
result = "\n".join(filtered)
print(result)
