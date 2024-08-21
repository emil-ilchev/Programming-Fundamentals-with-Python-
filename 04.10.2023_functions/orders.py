def orders(types, qty):
    if types == "coffee":
        return coffee_price * qty
    elif types == "coke":
        return coke_price * qty
    elif types == "water":
        return water_price * qty
    elif types == "snacks":
        return snacks_price * qty


coffee_price = 1.50
coke_price = 1.40
water_price = 1.00
snacks_price = 2.00

products = input()
quantity = int(input())
result = orders(products, quantity)
print(f"{result:.2f}")


def calculate_total_price(product, quantity):
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00
    else:
        return "Invalid product."

    total_price = price * quantity
    return total_price


product = input()
quantity = int(input())
total = calculate_total_price(product, quantity)
print(f"The total price for {quantity} {product}(s) is: ${total:.2f}")

# def calculate_total_price(product, quantity):
#     prices = {
#         "coffee": 1.50,
#         "water": 1.00,
#         "coke": 1.40,
#         "snacks": 2.00
#     }
#
#     if product in prices:
#         # Calculate the total price
#         total_price = prices[product] * quantity
#         return total_price
#     else:
#         return "Invalid product."
#
#
# product = input()
# quantity = int(input())
# total = calculate_total_price(product, quantity)
# print(f"The total price for {quantity} {product}(s) is: ${total:.2f}")
