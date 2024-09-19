employees = input().split()
happiness_factor = int(input())

employees = [int(x) * happiness_factor for x in employees]
average = sum(employees) / len(employees)
after_filtration = [num for num in employees if num >= average]

if len(after_filtration) >= len(employees) / 2:
    print(f"Score: {len(after_filtration)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(after_filtration)}/{len(employees)}. Employees are not happy!")


# employees = list(map(int, input().split()))
# happiness_factor = int(input())
#
# employees = [x * happiness_factor for x in employees]
# average = sum(employees) / len(employees)
# after_filtration = [num for num in employees if num >= average]
# if len(after_filtration) >= len(employees) / 2:
#     print(f"Score: {len(after_filtration)}/{len(employees)}. Employees are happy!")
# else:
#     print(f"Score: {len(after_filtration)}/{len(employees)}. Employees are not happy!")
