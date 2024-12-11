items = input().split()
searched = input().split()
bakery = {}

for i in range(0, len(items), 2):
    key = items[i]
    value = int(items[i + 1])
    bakery[key] = value

for product in searched:
    if product in bakery.keys():
        quantity = bakery[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
