def palindrome(palindrome_list):
    palindrome_list = palindrome_list.split(", ")
    new_list = palindrome_list[:: -1]
    return new_list == palindrome_list


palindrome_num = input()
result = palindrome(palindrome_num)
print("ok" if result else "not ok")
