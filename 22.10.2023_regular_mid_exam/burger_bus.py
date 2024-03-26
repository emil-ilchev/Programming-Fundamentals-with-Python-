cities = int(input())
profit = 0
total_profit = 0

for day in range(1, cities + 1):
    city_name = input()
    income = float(input())
    expenses = float(input())
    profit = income - expenses
    if day % 3 == 0:
        expenses *= 1.5
    # profit = income - expenses
    if day % 5 == 0:
        profit /= 1.1
    # profit = income - expenses
    print(f"In {city_name} Burger Bus earned {profit:.2f} leva.")
print(f"Burger Bus total profit: {total_profit:.2f} leva.")
