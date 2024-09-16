palindrome_list = input()
palindrome = input()
result = []
number = 0
for word in palindrome_list.split():
    if word == word[::-1]:
        result.append(word)

    if word == palindrome:
        number += 1
print(result)
print(f"Found palindrome {number} times")
