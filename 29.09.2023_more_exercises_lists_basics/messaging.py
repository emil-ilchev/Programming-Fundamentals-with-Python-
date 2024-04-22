numbers = input().split()
text = input()
message = ''
for number in numbers:
    digit_sum = sum(int(x) for x in number)
    index = digit_sum % len(text)
    char = text[index]
    message += char
    text = text[:index] + text[index + 1:]
print(message)
