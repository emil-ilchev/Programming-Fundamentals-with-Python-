n = int(input())
word = input()
full_list = []
include_word = []
for i in range(n):
    current_string = input()
    full_list.append(current_string)
    if word in current_string:
        include_word.append(current_string)

print(full_list)
print(include_word)

